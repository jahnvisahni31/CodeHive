# Problem Statement

You are given a table named `Views`, with the following schema:

| Column Name | Type  |
|-------------|-------|
| article_id  | int   |
| author_id   | int   |
| viewer_id   | int   |
| view_date   | date  |

There is no primary key for this table, and the table may have duplicate rows. Each row indicates that some viewer viewed an article (written by some author) on a specific date. Note that if `author_id` and `viewer_id` are equal, it indicates the same person.

Write an SQL query to find all the authors who viewed at least one of their own articles.

Return the result table sorted by `id` in ascending order.

### Example

Suppose the `Views` table contains the following rows:

| article_id | author_id | viewer_id | view_date |
|------------|-----------|-----------|-----------|
| 1          | 3         | 5         | 2022-01-01|
| 2          | 3         | 6         | 2022-02-01|
| 3          | 3         | 3         | 2022-03-01|
| 4          | 1         | 5         | 2022-04-01|
| 5          | 1         | 6         | 2022-05-01|

The authors who viewed at least one of their own articles are:

- Author 1
- Author 3

So, the output should be:

| id |
|----|
| 1  |
| 3  |

### Note

In the given examples, for the sake of simplicity, we assume that:
- There are no duplicate rows in the table.
