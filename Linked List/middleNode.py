class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        count = 0
        while current:
            current = current.next
            count += 1
        mid = count // 2 + 1
        while mid>1:
            head = head.next
            mid -= 1
        return head