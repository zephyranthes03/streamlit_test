from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return head

        prev, cur, ans = None, head, head.next
        while cur and cur.next:
            adj = cur.next
            if prev: prev.next = adj
            cur.next, adj.next = adj.next, cur
            prev, cur = cur, cur.next
        return ans or head

if __name__ == "__main__":
    input = ListNode(val=1, next=ListNode(val=1,next=None))
    solution = Solution()
    result = solution.swapPairs(input)
    print(f"Result: {result}")
