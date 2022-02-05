class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root: return ''
        q = deque([root])
        res = []
        while q:
            node = q.popleft()
            if not node:
                res.append('None')
            else:
                res.append(str(node.val))
                q.append(node.left)
                q.append(node.right)
        return ','.join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.


        :type data: str
        :rtype: TreeNode
        """
        if not data: return None
        vals = data.split(',')
        nodes = iter((None if val == 'None' else TreeNode(int(val)) for val in vals))
        root = next(nodes)
        q = deque([root])
        while q:
            node = q.popleft()
            left = next(nodes)
            if left:
                node.left = left
                q.append(left)
            right = next(nodes)
            if right:
                node.right = right
                q.append(right)
        return root