USE customeraccountloanDB;

-- create a table for customers.
DROP TABLE IF EXISTS dbo.customers;
CREATE TABLE dbo.customers (
           customer_id INT PRIMARY KEY,
           first_name VARCHAR(50),
           last_name VARCHAR(50),
           address VARCHAR(100),
           city VARCHAR(50),
           state VARCHAR(50),
           zip VARCHAR(20)
       );

-- create a table for accounts.
DROP TABLE IF EXISTS dbo.accounts;
 CREATE TABLE dbo.accounts (
           account_id INT PRIMARY KEY,
           customer_id INT,
           account_type VARCHAR(50),
           balance DECIMAL(10, 2),
           FOREIGN KEY (customer_id) REFERENCES  customers(customer_id)
       );

-- create a table for transactions.
DROP TABLE IF EXISTS dbo.transactions;
CREATE TABLE dbo.transactions (
           transaction_id INT PRIMARY KEY,
           account_id INT,
           transaction_date DATE,
           transaction_amount DECIMAL(10, 2),
           transaction_type VARCHAR(50),
           FOREIGN KEY (account_id) REFERENCES accounts(account_id)
       );

-- create a table for loans.
DROP TABLE IF EXISTS dbo.loans;
CREATE TABLE dbo.loans (
           loan_id INT PRIMARY KEY,
           customer_id INT,
           loan_amount DECIMAL(10, 2),
           interest_rate DECIMAL(5, 2),
           loan_term INT,
           FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
       );

-- create a table for loan_payments.
DROP TABLE IF EXISTS dbo.loan_payments;
CREATE TABLE dbo.loan_payments (
           payment_id INT PRIMARY KEY,
           loan_id INT,
           payment_date DATE,
           payment_amount DECIMAL(10, 2),
           FOREIGN KEY (loan_id) REFERENCES loans(loan_id)
       );


-- Querying all the columns in each table.
Select * from  dbo.customers;
Select * from  dbo.accounts;
Select * from  dbo.transactions;
Select * from  dbo.loans;
Select * from  dbo.loan_payments;

--4.1: Write query to retrieve all customer information:
Select * from  dbo.customers; 

-- 4.2: Query accounts for a specific customer:
select * from dbo.accounts 
where customer_id = 3; 


--4.3: Find the customer name and account balance for each account.
Select dbo.accounts.account_id,concat(dbo.customers.first_name, ' ' ,dbo.customers.last_name) as customer_name, dbo.accounts.balance  
from dbo.accounts 
left join dbo.customers 
on dbo.accounts.customer_id = dbo.customers.customer_id 
order by CAST(account_id AS INT) asc; 

--4.4: Analyze customer loan balances:
Select dbo.customers.customer_id, 
CONCAT(dbo.customers.first_name, ' ', dbo.customers.last_name) AS customer_name, 
SUM(cast(dbo.loans.loan_amount as decimal(18,2))) AS TotalLoanAmount 
from  
dbo.customers  
JOIN  
dbo.loans ON dbo.customers.customer_id = dbo.loans.customer_id 
GROUP BY 
dbo.customers.customer_id, dbo.customers.first_name, dbo.customers.last_name 
Order by  
TotalLoanAmount DESC; 


-- 4.5: List all customers who have made a transaction in the 2024-03. 
SELECT   
CONCAT(dbo.customers.first_name, ' ', dbo.customers.last_name) AS CustomerName 
FROM  
dbo.customers  
JOIN  
dbo.accounts ON dbo.customers.customer_id= dbo.accounts.customer_id 
JOIN  
dbo.transactions ON dbo.accounts.account_id = dbo.transactions.account_id 
WHERE  
dbo.transactions.transaction_date between '2024-03-01' AND '2024-03-31'; 



--5.1: Calculate the total balance across all accounts for each customer: 
Select dbo.customers.customer_id, concat(dbo.customers.first_name ,' ', dbo.customers.last_name) as customer_name, 
SUM(cast(dbo.accounts.balance as decimal(18,2))) as total_balance 
from dbo.accounts  
left join  
dbo.customers  
on dbo.accounts.customer_id = dbo.customers.customer_id 
group by dbo.customers.customer_id, dbo.customers.first_name, dbo.customers.last_name; 





--5.2:Calculate the average loan amount for each loan term:
Select avg(cast(loan_amount as decimal(18,2))) as avg_loan_amount, loan_term 
from dbo.loans 
group by loan_term; 



-- 5.3: Find the total loan amount and interest across all loans:
Select  SUM(cast(Loan_amount as decimal(18,2))) AS Total_Loan_Amount, 
SUM(cast(interest_rate as decimal(18,2))) AS TotalInterest 
FROM  
dbo.loans; 




--5.4:Find the most frequent transaction type.
SELECT  
transaction_type, 
COUNT(*) AS Frequency 
FROM  
dbo.transactions 
GROUP BY  
transaction_type; 




-- 5.5:Analyze transactions by account and transaction type:
SELECT  
dbo.accounts.account_id, 
dbo.transactions.transaction_type, 
COUNT(*) AS transaction_count, 
SUM(cast(dbo.transactions.transaction_amount as decimal(18,2))) AS TotalTransactionAmount 
FROM  
dbo.accounts  
JOIN  
dbo.transactions  ON dbo.accounts.account_id = dbo.transactions.account_id 
GROUP BY  
dbo.accounts.account_id, dbo.transactions.transaction_type 
ORDER BY  
dbo.accounts.account_id, transaction_count DESC; 




--6.1: Create a view of active loans with payments greater than $1000
DROP VIEW IF EXISTS ActiveLoansOver1000;

CREATE VIEW ActiveLoansOver1000 AS 
SELECT  
dbo.loans.loan_id, 
dbo.loans.customer_id, 
dbo.loans.loan_amount, 
dbo.loans.interest_rate, 
dbo.loan_payments.payment_amount, 
dbo.loan_payments.payment_date 
FROM  
dbo.loans  
JOIN  
dbo.loan_payments  ON dbo.loans .loan_id = dbo.loan_payments.loan_id 
WHERE   
dbo.loan_payments .payment_amount > 1000; 




--6.2: Create an index on `transaction_date` in the `transactions` table for performance optimization: 

CREATE INDEX IX_Transaction_Date 
ON transactions (transaction_date); 




