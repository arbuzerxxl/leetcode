from functools import reduce


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        cur = dummy = ListNode()
        while list1 and list2:
            if list1.val < list2.val:
                cur.next = list1
                list1, cur = list1.next, list1
            else:
                cur.next = list2
                list2, cur = list2.next, list2

        if list1 or list2:
            cur.next = list1 if list1 else list2

        return dummy.next


# data = [([1, 2, 4], [1, 3, 4]),
#         ([], []),
#         ([], [0]),
#         ]


# solve = Solution()
# for item in data:
#     print(solve.mergeTwoLists(list1=item[0], list2=item[1]))
