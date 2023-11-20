from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        nodes = []

        for i in range(len(lists)):
            node = lists[i]
            while node is not None:
                nodes.append(node)
                node = node.next

        nodes.sort(key=lambda x: x.val)
        nodes.append(None)

        for i in range(len(nodes) - 1):
            nodes[i].next = nodes[i+1]

        return nodes[0]
