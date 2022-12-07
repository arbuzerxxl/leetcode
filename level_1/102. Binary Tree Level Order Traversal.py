# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    data = []
    level = 0
    level_map = {}

    def levelOrder(self, root: TreeNode) -> list:

        self.data.clear()
        self.level = 0
        self.level_map.clear()

        if root is None:
            return self.data

        self.level_map[self.level] = [root.val]

        self.recursion(root=root)

        for value in self.level_map.values():
            self.data.append(value)

        return self.data

    def recursion(self, root):

        self.level += 1

        if root.left:

            if not self.level_map.get(self.level):
                self.level_map[self.level] = [root.left.val]
            else:
                self.level_map[self.level].append(root.left.val)

            self.recursion(root=root.left)

        if root.right:

            if not self.level_map.get(self.level):
                self.level_map[self.level] = [root.right.val]
            else:
                self.level_map[self.level].append(root.right.val)

            self.recursion(root=root.right)

        self.level -= 1


# TreeNode{val: 1, left: TreeNode{val: 2, left: TreeNode{val: 4, left: None, right: None}, right: None}, right: TreeNode{val: 3, left: None, right: TreeNode{val: 5, left: None, right: None}}}

# tree_5 = TreeNode()
# tree_5.val = 5

# tree_3 = TreeNode()
# tree_3.val = 3
# tree_3.right = tree_5

# tree_4 = TreeNode()
# tree_4.val = 4

# tree_2 = TreeNode()
# tree_2.val = 2
# tree_2.left = tree_4

# tree_1 = TreeNode()
# tree_1.val = 1
# tree_1.left = tree_2
# tree_1.right = tree_3

# TreeNode{val: 1, left: TreeNode{val: 2, left: TreeNode{val: 4, left: None, right: None}, right: TreeNode{val: 5, left: None, right: None}}, right: TreeNode{val: 3, left: None, right: None}}

tree_5 = TreeNode()
tree_5.val = 5

tree_3 = TreeNode()
tree_3.val = 3


tree_4 = TreeNode()
tree_4.val = 4

tree_2 = TreeNode()
tree_2.val = 2
tree_2.left = tree_4
tree_2.right = tree_5

tree_1 = TreeNode()
tree_1.val = 1
tree_1.left = tree_2
tree_1.right = tree_3
solve = Solution()
print(solve.levelOrder(root=tree_1))
