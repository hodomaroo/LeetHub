from typing import Optional

# Definition for a binary tree node.
 
class BSTIterator:
    #stack으로 구현하기
    def __init__(self, root: Optional[TreeNode]):
        self.nodeStack = [root]

    def next(self) -> int:
        while True:
            #print(self.nodeStack[-1].val,self.nodeStack)
            leftChild = self.nodeStack[-1].left
            rightChild = self.nodeStack[-1].right

            if leftChild:
                self.nodeStack[-1].left = None
                self.nodeStack.append(leftChild)

            else:
                
                node = self.nodeStack.pop()
                
                if rightChild:    
                    node.right = None
                    self.nodeStack.append(rightChild)

                return node.val

    def hasNext(self) -> bool:
        return True if self.nodeStack else False

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()