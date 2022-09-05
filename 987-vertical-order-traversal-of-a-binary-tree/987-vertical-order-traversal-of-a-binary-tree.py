# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        offsetQueue = deque([[]])
        offset = 0
        nodeId = 0
        
        information = []
        
        def dfs(node : TreeNode, pos : int, depth : int):
            nonlocal nodeId,offset
            if pos < offset:
                offset = pos
                offsetQueue.appendleft([nodeId])
                
            elif pos - offset >= len(offsetQueue):
                offsetQueue.append([nodeId])
            
            else:
                offsetQueue[pos - offset].append(nodeId)
            
            information.append((depth, node.val))
            nodeId += 1
            
            if node.left:
                dfs(node.left, pos - 1, depth + 1)
                
            if node.right:
                dfs(node.right, pos + 1, depth + 1)
            
        dfs(root, 0, 0)
            
        return [[information[i][1] for i in sorted(col, key = lambda x : information[x])] for col in offsetQueue]
        