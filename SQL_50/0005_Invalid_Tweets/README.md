# Problem Statement

You are given a table named `Tweets`, with the following schema:

| Column Name | Type    |
|-------------|---------|
| tweet_id    | int     |
| content     | varchar |

`tweet_id` is the primary key for this table, meaning each row has a unique `tweet_id`. This table contains all the tweets in a social media app.

Write an SQL query to find the IDs of the invalid tweets. A tweet is considered invalid if the number of characters used in its content is strictly greater than 15.

Return the result table in any order.

### Example

Suppose the `Tweets` table contains the following rows:

| tweet_id | content                          |
|----------|----------------------------------|
| 1        | Vote for Biden                   |
| 2        | Let us make America great again! |

The content length of the tweets are as follows:
- Tweet 1: Length = 14. It is a valid tweet.
- Tweet 2: Length = 32. It is an invalid tweet.

So, the output should be:

| tweet_id |
|----------|
| 2        |

### Note

In the given examples, for the sake of simplicity, we assume that:
- There are no duplicate rows in the table.
