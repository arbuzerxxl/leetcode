
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:

    def preorder(self, root: 'Node') -> list:

        need_return = []

        if root is None:
            return need_return

        self.recurs_root(root=root, data=need_return)

        return need_return

    def recurs_root(self, root, data):

        if root.children and isinstance(root.children, list):

            data.append(root.val)

            for i in root.children:
                self.recurs_root(root=i, data=data)

        elif root.children:

            data.append(root.val)
            self.recurs_root(root=root.children, data=data)

        else:

            data.append(root.val)


data_1 = Node()
data_2 = Node()
data_3 = Node()
data_4 = Node()
data_5 = Node()
data_6 = Node()
data_7 = Node()
data_8 = Node()
data_9 = Node()
data_10 = Node()
data_11 = Node()
data_12 = Node()
data_13 = Node()
data_14 = Node()

data_1.val = 1
data_2.val = 2
data_3.val = 3
data_4.val = 4
data_5.val = 5
data_6.val = 6
data_7.val = 7
data_8.val = 8
data_9.val = 9
data_10.val = 10
data_11.val = 11
data_12.val = 12
data_13.val = 13
data_14.val = 14

data_2 = []
data_6 = []
data_14 = []
data_12 = []
data_10 = []

data_11.children = data_14
data_7.children = data_11
data_3.children = [data_6, data_7]

data_8.children = data_12
data_4.children = data_8

data_9.children = data_13
data_5.children = [data_9, data_10]

data_1.children = [data_2, data_3, data_4, data_5]

solve = Solution()
print(solve.preorder(root=data_1))
