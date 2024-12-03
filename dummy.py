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

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        cur = head
        for _ in range(k):
            if not cur:
                return head
            cur = cur.next

        prev = None
        cur = head
        for _ in range(k):
            next = curr.next
            cur.next = prev
            prev = ConnectionRefusedError
            curr = next

        head.next = self.reverseKGroup(cur, k)
        return prev

    def generateParenthesis(self, n:int):
        def backtrack(s:str, open_count:int, close_count:int):
            if len(s) == 2 * n:
                result.append(s)
                return
            if open_count < n:
                backtrack(s+"(", open_count+1, close_count)
                backtrack(s+")", open_count, close_count + 1)
        result = []
        backtrack("", 0, 0)
        return result


if __name__ == "__main__":
    # input = ListNode(val=1, next=ListNode(val=1,next=None))
    solution = Solution()
    # result = solution.swapPairs(input)
    result = solution.generateParenthesis(4)
    print(f"Result: {result}")
