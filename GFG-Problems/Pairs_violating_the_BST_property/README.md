## Pairs Violating BST Property

### Problem Statement
Given a binary tree with n nodes, find the number of pairs violating the Binary Search Tree (BST) property.

#### BST Properties:
1. Every node is greater than its left child and less than its right child.
2. Every node is greater than the maximum value in its left subtree and less than the minimum value in its right subtree.
3. The maximum in the left subtree must be less than the minimum in the right subtree.

### Example

#### Input
n = 5

Input tree:
       10
      /  \
     50  20
    / \
   30  40

#### Output
5

#### Explanation
Pairs violating BST property are:
- (10,50): 10 should be greater than its left child value.
- (40,30): 40 should be less than its right child value.
- (50,20), (50,30), and (50,40): maximum of left subtree of 10 is 50 greater than 20, 30, and 40 of its right subtree.

### Constraints
- 1 <= n <= 2*10^4
- -10^9 <= node->data <= 10^9

### Approach
1. Traverse the tree and store the inorder traversal in an array.
2. Count the number of pairs violating the BST property by iterating through the array and checking for violations.

### Code (C++)
*Not provided in this markdown. See the actual code implementation in your programming environment.*

### Complexity Analysis
- Time complexity: O(n*logn) due to sorting the inorder traversal.
- Space complexity: O(n) for storing the inorder traversal.
