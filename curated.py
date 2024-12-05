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

Max_file_info = max(dbutils.fs.ls("abfss://rawdata@projectdatabricks98.dfs.core.windows.net/data/sales_data.csv/"))
print(Max_file_info.path)

# COMMAND ----------

df = spark.read.csv(Max_file_info.path, header=True, inferSchema="true")
display(df)

# COMMAND ----------

from pyspark.sql import SparkSession
from pyspark.sql.functions import initcap

df = df.withColumn("Product", initcap(df["Product"])).withColumn("Region", initcap(df["Region"]))
display(df)

# COMMAND ----------

from pyspark.sql import SparkSession
from pyspark.sql.functions import initcap,col, abs, when

df=df.withColumn(
    "Quantity",when(col("quantity").isNull(), 0).otherwise(abs(col("quantity"))))
display(df)

# COMMAND ----------

from pyspark.sql import SparkSession
from pyspark.sql.functions import regexp_replace, col

df=df.withColumn("UnitPrice",regexp_replace(col("Price Per Unit"), r"\$", ""))
df = df.drop("Price Per Unit")
display(df)


# COMMAND ----------

from pyspark.sql import SparkSession
from pyspark.sql.functions import col, to_date, coalesce
df= df.withColumn("TransactionDate", 
    coalesce(
        to_date(col("Transaction Date"), "yyyy-MM-dd"),
        to_date(col("Transaction Date"), "MM-dd-yyyy"),
        to_date(col("Transaction Date"), "yyyy-MM-dd"),
        to_date(col("Transaction Date"), "dd/MM/yyyy"),
        to_date(col("Transaction Date"), "MM/dd/yyyy")
    )
)
df = df.drop("Transaction Date")
display(df)

# COMMAND ----------

from pyspark.sql import SparkSession
df=df.withColumnRenamed("Transaction ID", "TransactionID").withColumnRenamed("Customer Name", "CustomerName")
display(df)

# COMMAND ----------

# Step 1: Write the DataFrame to the directory
df.coalesce(1).write.format("csv").mode("overwrite").option("header", "true").save("abfss://curated@projectdatabricks98.dfs.core.windows.net/curateddata")




# COMMAND ----------

# Step 2: Define the paths
source_path = "abfss://curated@projectdatabricks98.dfs.core.windows.net/curateddata/"
destination_path = "abfss://curated@projectdatabricks98.dfs.core.windows.net/curated_renamed/curated_sales_data.csv"

# Step 3: List the files in the source directory
files = dbutils.fs.ls(source_path)

# Step 4: Find the file that matches the pattern
source_file_path = None
for file in files:
    if "part-00000" in file.name:
        source_file_path = file.path
        break

# Step 5: Rename the part file to the desired name
if source_file_path:
    dbutils.fs.mv(source_file_path, destination_path)
else:
    raise FileNotFoundError("The specified file part-00000 was not found in the source directory.")

# Step 6: Clean up the original directory
#dbutils.fs.rm(source_path, recurse=True)
