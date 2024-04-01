# SQL Query to Find Products that are Low Fat and Recyclable

Given a SQL database schema with a table named Products, the task is to find the IDs of products that are both low fat and recyclable. Below is the schema of the Products table:

| Column Name | Type   |
|-------------|--------|
| product_id  | int    |
| low_fats    | enum   |
| recyclable  | enum   |

`product_id` is the primary key for this table. `low_fats` and `recyclable` are ENUM types with values 'Y' or 'N', indicating whether the product is low fat or recyclable respectively.

## Example

**Input:**

Products table:

| product_id | low_fats | recyclable |
|------------|----------|------------|
| 0          | Y        | N          |
| 1          | Y        | Y          |
| 2          | N        | Y          |
| 3          | Y        | Y          |
| 4          | N        | N          |

**Output:**

| product_id |
|------------|
| 1          |
| 3          |

Explanation: Only products 1 and 3 are both low fat and recyclable.

