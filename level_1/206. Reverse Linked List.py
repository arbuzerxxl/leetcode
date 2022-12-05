# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def reverseList(self, head):
        # Initialize prev pointer as NULL...
        prev = None
        # Initialize the curr pointer as the head...
        curr = head
        # Run a loop till curr points to NULL...
        while curr:
            # Initialize next pointer as the next pointer of curr...
            next = curr.next
            # Now assign the prev pointer to curr’s next pointer.
            curr.next = prev
            # Assign curr to prev, next to curr...
            prev = curr
            curr = next
        return prev       # Return the prev pointer to get the reverse linked list...


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
solve.reverseList(head=data)





# ListNode{val: 1, next: ListNode{val: 2, next: ListNode{val: 3, next: ListNode{val: 4, next: ListNode{val: 5, next: None}}}}}