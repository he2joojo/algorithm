from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1, num2 = 0, 0
        multiple = 1
        while l1 != None:
            num1 += (l1.val * multiple)
            multiple *= 10
            l1 = l1.next
        multiple = 1
        while l2 != None:
            num2 += (l2.val * multiple)
            multiple *= 10
            l2 = l2.next

        score = num1 + num2
        head = tmp = ListNode()

        while score >= 0:
            tmp.next = ListNode(score % 10)
            tmp = tmp.next
            score = score // 10
            if score == 0:
                break
        return head.next

