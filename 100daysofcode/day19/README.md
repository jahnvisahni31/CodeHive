# Minimum Remove to Make Parentheses Valid

## Problem Statement

Given a string `s` of '(', ')', and lowercase English characters.

Your task is to remove the minimum number of parentheses ('(' or ')', in any positions) so that the resulting parentheses string is valid and return any valid string.

Formally, a parentheses string is valid if and only if:

- It is the empty string, contains only lowercase characters, or
- It can be written as AB (A concatenated with B), where A and B are valid strings, or
- It can be written as (A), where A is a valid string.

### Examples

Example 1:

Input: 

s = "lee(t(c)o)de)"

Output: 

"lee(t(c)o)de"

Explanation: "lee(t(co)de)", "lee(t(c)ode)" would also be accepted.

### Constraints

- 1 <= s.length <= 10^5
- `s[i]` is either '(', ')', or lowercase English letter.

## Approach

To solve this problem, we can use a stack to keep track of the indices of opening parentheses. Iterate through the string, and if an opening parentheses is encountered, push its index onto the stack. If a closing parentheses is encountered, check if the stack is empty. If it's not empty, pop an index from the stack. If it's empty, mark the current index for removal. After processing the string, any remaining indices in the stack correspond to unmatched opening parentheses that should be removed. Finally, construct the resulting string excluding the marked indices.
