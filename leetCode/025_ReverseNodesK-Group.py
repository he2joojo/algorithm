from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # 리스트에 노드 담기
        nodes = []
        node = head
        while node is not None:
            nodes.append(node)
            node = node.next

        # 노드 순서 바꾸기
        n = len(nodes) // k
        for i in range(n):
            idx = i * k

            front = nodes[:idx]
            tmp = nodes[idx:idx + k]
            tmp.reverse()
            back = nodes[idx + k:]

            nodes = front + tmp + back

        # 노드 참조 바꾸기
        n = len(nodes)
        nodes.append(None)
        for i in range(n):
            nodes[i].next = nodes[i + 1]

        return nodes[0]
