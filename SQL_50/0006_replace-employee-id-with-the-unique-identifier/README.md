# Problem Statement

You are given two tables, `Employees` and `EmployeeUNI`, with the following schemas:

**Employees:**

| Column Name | Type    |
|-------------|---------|
| id          | int     |
| name        | varchar |

`id` is the primary key for this table, meaning each row has a unique `id`. Each row contains the `id` and the `name` of an employee in a company.

**EmployeeUNI:**

| Column Name | Type    |
|-------------|---------|
| id          | int     |
| unique_id   | int     |

`(id, unique_id)` is the primary key for this table, a combination of columns with unique values. Each row contains the `id` and the corresponding `unique_id` of an employee in the company.

Write an SQL query to show the unique ID of each user. If a user does not have a unique ID, replace it with `null`.

Return the result table in any order.

### Example

Suppose the `Employees` table contains the following rows:

| id | name     |
|----|----------|
| 1  | Alice    |
| 7  | Bob      |
| 11 | Meir     |
| 90 | Winston  |
| 3  | Jonathan |

And the `EmployeeUNI` table contains the following rows:

| id | unique_id |
|----|-----------|
| 3  | 1         |
| 11 | 2         |
| 90 | 3         |

The output should be:

| unique_id | name     |
|-----------|----------|
| null      | Alice    |
| null      | Bob      |
| 2         | Meir     |
| 3         | Winston  |
| 1         | Jonathan |

Explanation:

- Alice and Bob do not have a unique ID, so we show `null` instead.
- The unique ID of Meir is 2.
- The unique ID of Winston is 3.
- The unique ID of Jonathan is 1.

### Note

In the given examples, for the sake of simplicity, we assume that:
- There are no duplicate rows in the tables.
