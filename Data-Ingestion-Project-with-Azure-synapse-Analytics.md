Data Ingestion Project with Azure Synapse Analytics.

Here are the steps which I followed to create a data driven workflow using Azure Synapse Analytics.

Step 1:Pre-requisites for Data Ingestion Pipeline.

Login to Azure portal using login credentials. 

Created a resource group “charitharesources” for the services to use in Azure portal. 

Created an Azure SQL Database “adventuredb“, Azure SQL server and use sample data “AdventureWorks” to ingest data into storage account. 

Created an Azure synapse Analytics workspace “charithaworkspace” along with storage account “suchistorage98” and container named “raw-data” to use.
Create Azure key Vault to ingest data from SQL DB.

Created an Azure Key Vault with the name  “charithavault” using create resource. 
![image](https://github.com/user-attachments/assets/1dffe37a-2836-425c-8a56-92d21cbba37b)


Configure the key vault by generating a secret a key for Azure synapse.
![image](https://github.com/user-attachments/assets/4bdee8a8-d805-4576-8b6e-907ad4160fe7)


Enable the access policies for the resources to use Azure Synapse analytics and add managed identity object of synapse workspace to the key vault.
![image](https://github.com/user-attachments/assets/f007ccd3-1bfa-4983-aaf2-944d014d08fa)


Enable the the system assigned managed identity in the SQL server for the SQL DB to use the azure key vault security system. 
![image](https://github.com/user-attachments/assets/3fa702af-4ac3-477b-96c9-3eb23106270c)

Step 2:Create the data driven pipeline (data ingestion) using dynamic parameters. 

Launch synapse workspace to create data driven pipeline. 
Created the linked service for SQL DB “ls_module3_sqldb”, key vault “ls_module3_keyvault” and storage account “ls_module3_storage”.
![image](https://github.com/user-attachments/assets/e42f21e7-a096-43fe-b29f-27c72725d9a5)


While creating linked service for SQL DB, select azure key vault instead of azure SQL authentication.
![image](https://github.com/user-attachments/assets/5ebc39ea-5c58-4694-8fa0-0cb1a0d02329)


Created datasets for SQL DB and Storage accounts with the names “ds_module3_sqldb” and “ds_module3_storage”. 
After creating datasets, created parameters for source table and database with the names “srcDB” and “srcTable”. 
Connected these parameters dynamically to the datasets.
![image](https://github.com/user-attachments/assets/2448ffc3-5f1b-4ffd-8545-25419ff08359)


Created the parameters “targettable” and “targetFolder”  for the storage account dataset and connected the created parameters dynamically to the storage dataset.
We have also set the file name dynamically using functions like utcNow() and concat().
![image](https://github.com/user-attachments/assets/6598e65a-448d-4a75-a8c1-8ab17679ab28)


Created pipeline by copy data activity and initialized pipeline level parameters as “targetDB” and “targetTable
![image](https://github.com/user-attachments/assets/9dd59164-7e07-4903-b31e-99f40efdf295)

Connected the parameters dynamically to the source and sink to the pipeline for copy data activity.
![image](https://github.com/user-attachments/assets/1dae4cce-7b1d-4e1b-9a41-95135a79399d)
![image](https://github.com/user-attachments/assets/3efbc09c-afce-44ac-9aae-05d9eb161b7e)

Pass the values dynamically to the pipeline level parameters(copy data activity) to debug the pipeline and publish the changes to Azure.
![image](https://github.com/user-attachments/assets/13de33a4-6881-4671-88b6-d891597bc7cf)

Pipeline is successfull and copied the data from Azure SQL DB to Storage account and created a file in the container for schema and table which we passed as parameters.
![image](https://github.com/user-attachments/assets/943eff08-00fc-4d29-b0b6-2a34a53c2e3e)

Created a schedule event trigger to schedule the pipeline based on time intervals(eg: 5 minuites) to fetch the data.
![image](https://github.com/user-attachments/assets/4e5fbc34-8e30-4f09-a835-933468e4db0e)
![image](https://github.com/user-attachments/assets/ea2a372b-ec22-4c2d-b452-6c40f654a3cd)

Step 3:Create a synapse external table using serverless SQL pool.
For Silver or Gold stage data, created a Synapse External Table. Specified the format, source, and table definition to make the data queryable.

Create External File Format.
The external file format defines the structure of the data files that Azure Synapse will read. We will use a delimited text format where the fields are separated by commas.
Create the external data source.
The external data source points to the storage account where the data files are located. In this case, it's an Azure Data Lake Storage Gen2 account.
![image](https://github.com/user-attachments/assets/e33888fb-98a1-4e97-9dfb-01e712e4311c)


Create the external table.
The external table maps to the data files stored in Azure Data Lake. This allows us to query the data without physically loading it into the dedicated SQL pool.
![image](https://github.com/user-attachments/assets/52431b32-5728-43fa-9735-e073a58b2431)

Step 4: Data Exploration with external table.

Refer to the SQL script "SQLqueryforModule2.sql" file.

Result for the queries are attached below.

--Query 1

--select all the data from the table customer.

SELECT * from customer
![image](https://github.com/user-attachments/assets/d0ce54f3-6d23-47d0-ba1a-58652bc27008)


--Query 2

--Get the customers who has the latest modified date.

SELECT CustomerID, FirstName, LastName, ModifiedDate
FROM customer
ORDER BY ModifiedDate DESC;
![image](https://github.com/user-attachments/assets/e1c867f9-083d-477f-a1e4-1a164cd63590)



--Query 3

--Find customers who have been modified after a specific date, grouped by SalesPerson.

SELECT SalesPerson, COUNT(CustomerID) AS CustomerCount
FROM customer
WHERE ModifiedDate > '"2005-01-01"'
GROUP BY SalesPerson;
![image](https://github.com/user-attachments/assets/9bbde359-2637-4e3a-9405-e3a2328e71cb)


--Query 4

--Select customers whose last name contains a specific substring (e.g., 'Haines').

SELECT CustomerID, FirstName, LastName 
FROM customer
WHERE LastName LIKE '%Haines%';
![image](https://github.com/user-attachments/assets/f55ce0ea-6c1d-45db-b72b-d65f8cc3f267)


--Query 5

--Get customers with a specific domain in their email address (e.g., adventure-works.com).

SELECT CustomerID, FirstName, LastName, EmailAddress
FROM customer
WHERE EmailAddress LIKE '"%@adventure-works.com"';
![image](https://github.com/user-attachments/assets/f7b7dd99-92f8-4d7a-9e47-89d97bc98ac3)


--Query 6

--Get customers who have a rowguid matching a specific value.

SELECT CustomerID, FirstName, LastName, rowguid
FROM customer
WHERE rowguid ='3f5ae95e-b87d-4aed-95b4-c3797afcb74f';
![image](https://github.com/user-attachments/assets/0a09dd8e-8a4f-421d-b7b5-4b3f1ea9cce9)














