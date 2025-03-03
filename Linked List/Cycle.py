class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        dic = {}
        while head:
            if dic.get(head):
                dic[head] += 1
            else:
                dic[head] = 1
            if dic[head] > 1:
                return True
            head = head.next
        return False