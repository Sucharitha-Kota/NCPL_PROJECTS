IF NOT EXISTS (SELECT * FROM sys.external_file_formats WHERE name = 'SynapseDelimitedTextFormat') 
	CREATE EXTERNAL FILE FORMAT [SynapseDelimitedTextFormat] 
	WITH ( FORMAT_TYPE = DELIMITEDTEXT ,
	       FORMAT_OPTIONS (
			 FIELD_TERMINATOR = ',',
			 FIRST_ROW = 2,
			 USE_TYPE_DEFAULT = FALSE
			))
GO

IF NOT EXISTS (SELECT * FROM sys.external_data_sources WHERE name = 'raw-data_suchistorage98_dfs_core_windows_net') 
	CREATE EXTERNAL DATA SOURCE [raw-data_suchistorage98_dfs_core_windows_net] 
	WITH (
		LOCATION = 'abfss://raw-data@suchistorage98.dfs.core.windows.net' 
	)
GO

CREATE EXTERNAL TABLE customer (
	[CustomerID] NVARCHAR(1000),
	[NameStyle] NVARCHAR(1000),
	[Title] NVARCHAR(1000),
	[FirstName] nvarchar(1000),
	[MiddleName] nvarchar(1000),
	[LastName] nvarchar(1000),
	[Suffix] nvarchar(1000),
    [CompanyName] nvarchar(1000),
    [SalesPerson] nvarchar(1000),
    [EmailAddress] nvarchar(1000),
    [Phone] nvarchar(1000),
    [PasswordHash] nvarchar(1000),
    [PasswordSalt] nvarchar(1000),
    [rowguid] nvarchar(1000),
    [ModifiedDate] nvarchar(1000)
	)
	WITH (
	LOCATION = '/SalesLT/Customer/',
	DATA_SOURCE = [raw-data_suchistorage98_dfs_core_windows_net],
	FILE_FORMAT = [SynapseDelimitedTextFormat]
	)
GO
