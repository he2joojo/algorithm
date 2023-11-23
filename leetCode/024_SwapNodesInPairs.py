from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 리스트에 노드 담기
        nodes = []
        node = head
        while node is not None:
            nodes.append(node)
            node = node.next

        # 순서 바꾸기
        n = len(nodes) // 2
        for i in range(n):
            idx = i * 2
            tmp = nodes[idx]
            nodes[idx] = nodes[idx + 1]
            nodes[idx + 1] = tmp

        # 노드 참조 바꾸기
        n = len(nodes)
        nodes.append(None)
        for i in range(n):
            nodes[i].next = nodes[i+1]

        return nodes[0]
