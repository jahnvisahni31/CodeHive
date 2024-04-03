# Kth Common Ancestor in Binary Search Tree

## Problem Statement

Given a Binary Search Tree (BST) with `n` (where n ≥ 2) nodes, find the kth common ancestor of nodes x and y in the given tree. Return -1 if the kth ancestor does not exist.

Nodes x and y will always be present in the input of a BST, and x ≠ y.

### Example 1:

Input:
50
/
30 70
/ \ /
20 40 60 80

k = 2, x = 40, y = 60

Output:
30

Explanation:
Their 2nd common ancestor is 30.

shell
Copy code

### Example 2:

Input:
50
/
30 70
/ \ /
20 40 60 80

k = 2, x = 40, y = 60

Output:
-1

Explanation:
LCA of 40 and 60 is 50, which is root itself. There does not exist a 2nd common ancestor in this case.

csharp
Copy code

## Function Signature

```cpp
int kthCommonAncestor(Node* root, int k, int x, int y)
```
Constraints
1 ≤ n, k ≤ 10^5
1 ≤ node->data, x, y ≤ 10^9

Approach to Solution
1. Traverse the BST to find the lowest common ancestor (LCA) of nodes x and y.
2. Store the path from the root to the LCA for both x and y.
3. Traverse both paths simultaneously to find the kth common ancestor.
4. If the kth ancestor exists, return it; otherwise, return -1.

Time and Space Complexity

Time Complexity: O(height of the tree)
Space Complexity: O(height of the tree)

Contributing
Contributions are welcome. Feel free to raise issues and submit pull requests.

References
Binary Search Tree
Lowest Common Ancestor
