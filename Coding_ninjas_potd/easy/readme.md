## Zig-Zag Pattern String

You are given a string `STR` of size `N` and an integer `M` (the number of rows in the zig-zag pattern of `STR`). Your task is to return the string formed by concatenating all `M` rows when string `STR` is written in a row-wise zig-zag pattern.

### Example:

- **Input:**  
  - `N = 12`,  
  - `M = 3`, and  
  - `STR = 'CODINGNINJAS'`

- **Output:**  
  The string formed by concatenating all `M` rows is `CNNOIGIJSDNA`.

Explanation:  
There are three rows (`M = 3`) in the zig-zag pattern.  
- Row one contains `CNN`.  
- Row two contains `OIGIJS`.  
- Row three contains `DNA`.  
After concatenating the three rows, we get the string `CNNOIGIJSDNA`.

**Note:**
- The string `STR` consists of capital letters only (i.e., characters from `A-Z`).
