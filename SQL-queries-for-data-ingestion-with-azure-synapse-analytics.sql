--query 1
SELECT * from customer

--query 2
SELECT CustomerID, FirstName, LastName, ModifiedDate
FROM customer
ORDER BY ModifiedDate DESC;

--query 3
SELECT SalesPerson, COUNT(CustomerID) AS CustomerCount
FROM customer
WHERE ModifiedDate > '"2005-01-01"'
GROUP BY SalesPerson;

--query 4
SELECT CustomerID, FirstName, LastName 
FROM customer
WHERE LastName LIKE '%Haines%';

--query 5
SELECT CustomerID, FirstName, LastName, EmailAddress
FROM customer
WHERE EmailAddress LIKE '"%@adventure-works.com"';

--query 6
SELECT CustomerID, FirstName, LastName, rowguid
FROM customer
WHERE rowguid ='3f5ae95e-b87d-4aed-95b4-c3797afcb74f';

