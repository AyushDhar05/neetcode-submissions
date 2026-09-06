# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return None
        # # iterative
        # prev = None
        # curr = head

        # while curr:
        #     nxt = curr.next
        #     curr.next = prev
        #     prev = curr
        #     curr = nxt

        # return prev

        # recursive
        new_head = None
        def helper(head):
            nonlocal new_head
            if head.next:
                helper(head.next)
                head.next.next = head
                head.next = None
            else:
                new_head = head

        helper(head)
        return new_head


