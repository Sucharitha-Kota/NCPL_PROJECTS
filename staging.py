# Databricks notebook source
application_id="ea574ce4-9be1-4b00-a0e4-1399cfdff23e"
directory_id="17e46124-a380-4096-841f-150cd2c41f95"
service_credential = dbutils.secrets.get('secret-scope','servicecredential')

spark.conf.set("fs.azure.account.auth.type.projectdatabricks98.dfs.core.windows.net", "OAuth")
spark.conf.set("fs.azure.account.oauth.provider.type.projectdatabricks98.dfs.core.windows.net", "org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider")
spark.conf.set("fs.azure.account.oauth2.client.id.projectdatabricks98.dfs.core.windows.net", application_id)
spark.conf.set("fs.azure.account.oauth2.client.secret.projectdatabricks98.dfs.core.windows.net", service_credential)
spark.conf.set("fs.azure.account.oauth2.client.endpoint.projectdatabricks98.dfs.core.windows.net", f"https://login.microsoftonline.com/{directory_id}/oauth2/token")

# COMMAND ----------

display(dbutils.fs.ls("abfss://curated@projectdatabricks98.dfs.core.windows.net/curated_renamed/"))

# COMMAND ----------

from pyspark.sql import functions as F
from pyspark.sql.types import *

sales_schema = StructType([
    StructField("TransactionID",StringType(), True),
    StructField("CustomerName",StringType(), True),
    StructField("Product", StringType(), True),
    StructField("Quantity",DoubleType(), True),
    StructField("Region", StringType(), True),
    StructField("UnitPrice", DoubleType(), True),
    StructField("TransactionDate", DateType(), True)
])

df = spark.read.csv(
    "abfss://curated@projectdatabricks98.dfs.core.windows.net/curated_renamed/curated_sales_data.csv",
    header=True,
    schema=sales_schema
)
df.printSchema()

# COMMAND ----------

from pyspark.sql.functions import expr, year,col

# Clean Price Per Unit and derive Total Amount
df = df.withColumn("TotalAmount", col("Quantity") * col("UnitPrice"))

# Add Transaction Year
df = df.withColumn("TransactionYear", year(col("TransactionDate")))

# Write to Delta Lake
#df.write.format("csv").mode("overwrite").option("header", "true").save("abfss://staging@projectdatabricks98.dfs.core.windows.net/staging_sales_data.csv")

display(df)

# COMMAND ----------

df.write.partitionBy("Product").parquet("abfss://staging@projectdatabricks98.dfs.core.windows.net/staging_sales_data.parquet")
