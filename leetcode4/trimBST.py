class Solution(object):
    def trimBST(self, root, L, R):
        # def trim(node):
        #     if not node:
        #         return None
        #     elif node.val > R:
        #         return trim(node.left)
        #     elif node.val < L:
        #         return trim(node.right)
        #     else:
        #         node.left = trim(node.left)
        #         node.right = trim(node.right)
        #         return node
        #
        # return trim(root)


# //////////////////////////////////////////
            if not root:
                return None

            if root.val < L:
                return self.trimBST(root.right, L, R)
            elif root.val > R:
                return self.trimBST(root.left, L, R)
            else:
                root.left = self.trimBST(root.left, L, R)
                root.right = self.trimBST(root.right, L, R)
                return root
