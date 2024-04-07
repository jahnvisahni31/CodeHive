# Valid Parenthesis String

Given a string `s` containing only three types of characters: `'('`, `')'`, and `'*'`, determine if the string is valid according to certain rules.

## Problem Description

The following rules define a valid string:

- Any left parenthesis `'('` must have a corresponding right parenthesis `')'`.
- Any right parenthesis `')'` must have a corresponding left parenthesis `'('`.
- Left parenthesis `'('` must occur before the corresponding right parenthesis `')'`.
- The character `'*'` can be treated as a single right parenthesis `')'`, a single left parenthesis `'('`, or an empty string `""`.

### Examples

**Example 1:**

Input: `s = "()"`

Output: `true`

**Example 2:**

Input: `s = "(*)"`

Output: `true`

**Example 3:**

Input: `s = "(*))"`

Output: `true`

### Constraints

- 1 <= s.length <= 100
- s[i] is `'('`, `')'`, or `'*'`.

## Approach

To solve this problem, we can use a greedy algorithm. We'll keep track of two values: the minimum and maximum possible number of open left parenthesis at any point while traversing the string.

- If we encounter a `'('`, both the minimum and maximum possible left parenthesis count increase.
- If we encounter a `')'`, both the minimum and maximum possible left parenthesis count decrease, but the minimum can't go below 0.
- If we encounter a `'*'`, the maximum possible left parenthesis count increases, as it can be treated as a `'('`, and the minimum possible left parenthesis count decreases, as it can be treated as a `')'`.

At the end, if the minimum possible left parenthesis count is 0, the string is valid.
