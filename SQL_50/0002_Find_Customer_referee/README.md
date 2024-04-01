# SQL Query to Find Customers Not Referred by Customer with ID = 2

Given a SQL database schema with a table named Customer, the task is to find the names of customers who are not referred by the customer with ID = 2. Below is the schema of the Customer table:

| Column Name | Type    |
|-------------|---------|
| id          | int     |
| name        | varchar |
| referee_id  | int     |

In SQL, `id` is the primary key column for this table. Each row of this table indicates the ID of a customer, their name, and the ID of the customer who referred them.

## Example

**Input:**

Customer table:

| id | name | referee_id |
|----|------|------------|
| 1  | Will | null       |
| 2  | Jane | null       |
| 3  | Alex | 2          |
| 4  | Bill | null       |
| 5  | Zack | 1          |
| 6  | Mark | 2          |

**Output:**

| name |
|------|
| Will |
| Jane |
| Bill |
| Zack |

Explanation: Customers Will, Jane, Bill, and Zack are not referred by customer with ID = 2.

