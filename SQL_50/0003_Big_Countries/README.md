# Problem Statement

You are given a table named `World`, with the following schema:

| Column Name | Type    |
|-------------|---------|
| name        | varchar |
| continent   | varchar |
| area        | int     |
| population  | int     |
| gdp         | bigint  |

`name` is the primary key for this table, meaning each row has a unique `name`. Each row provides information about a country, including its name, the continent to which it belongs, its area in square kilometers, its population, and its GDP value.

A country is considered big if it satisfies at least one of the following conditions:
1. It has an area of at least three million square kilometers (i.e., 3,000,000 km²).
2. It has a population of at least twenty-five million people (i.e., 25,000,000).

Write an SQL query to find the name, population, and area of the big countries.

Return the result table in any order.

### Example

Suppose the `World` table contains the following rows:

| name      | continent | area    | population | gdp       |
|-----------|-----------|---------|------------|-----------|
| USA       | North     | 9372610 | 331002651  | 214033000 |
| Canada    | North     | 9984670 | 38005238   | 1785387   |
| Russia    | Europe    | 17098242| 146793744  | 22617495  |
| China     | Asia      | 9596960 | 1439323776 | 14140163  |
| Australia | Australia | 7692024 | 25499884   | 1408676   |

The big countries are:

- USA: Population - 331002651, Area - 9372610
- Russia: Population - 146793744, Area - 17098242
- China: Population - 1439323776, Area - 9596960
- Australia: Population - 25499884, Area - 7692024

So, the output should be:

| name      | population | area    |
|-----------|------------|---------|
| USA       | 331002651  | 9372610 |
| Russia    | 146793744  | 17098242|
| China     | 1439323776 | 9596960 |
| Australia | 25499884   | 7692024 |

### Note

In the given examples, for the sake of simplicity, we assume that:
- The `name` column is the primary key for this table, ensuring uniqueness.
- There are no duplicate rows in the table.
