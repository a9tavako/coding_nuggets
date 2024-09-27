from typing import Dict, Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack = [] # The nodes in the stack form the path to the current node
        # but excluding the nodes that have already been iterated. 
        current = root
        while current:
            self.stack.append(current)
            current = current.left

    def _advance(self):
        if not self.hasNext():
            raise StopIteration("No next element in the iterator")

        current = self.stack.pop()
        if current.right:
            current = current.right
            while current:
                self.stack.append(current)
                current = current.left
            return

    def next(self) -> int:
        to_return = self.stack[-1].val
        self._advance()
        return to_return

    def hasNext(self) -> bool:
        return len(self.stack) > 0

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()