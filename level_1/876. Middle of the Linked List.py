# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        if not head.next:
            return head

        counter_head = head

        counter = 0

        while counter_head.next:
            counter += 1
            counter_head = counter_head.next

        counter += 1

        middle = counter // 2 + 1  # if counter % 2 == 0 else counter // 2 + 1

        for i in range(1, middle):
            head = head.next

        return head


data = ListNode()
data.val = 1
data.next = ListNode()
data.next.val = 2
data.next.next = ListNode()
data.next.next.val = 3
data.next.next.next = ListNode()
data.next.next.next.val = 4
data.next.next.next.next = ListNode()
data.next.next.next.next.val = 5


solve = Solution()
solve.middleNode(head=data)
