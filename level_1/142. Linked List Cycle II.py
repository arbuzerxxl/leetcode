# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def detectCycle(self, head):
        slow = fast = head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
            if slow == fast: break
        else: return None  # if not (fast and fast.next): return None
        while head != slow:
            head, slow = head.next, slow.next
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
solve.detectCycle(head=data)
