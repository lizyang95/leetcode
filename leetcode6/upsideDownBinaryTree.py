# Here is a small point to be noticed, when you connect the root to the right subtree, you need to make sure you are not copying the original root, otherwise it will become cyclic!
class Solution(object):
    def upsideDownBinaryTree(self, root):
        if (not root) or (not root.left):
            return root
        newroot = self.upsideDownBinaryTree(root.left)
        root.left.left = rootlright
        root.left.right = root
        root.left = None
        root.right = None
        return newroot


    def upsideDownBinaryTree_iterative(self,root):
        curr = root
        next = None
        temp = None
        prev = None
        while curr:
            next = curr.left
            # swapping nodes now, need temp to keep the previous right child
            curr.left = temp
            temp = curr.right
            curr.right = prev

            prev = curr
            curr = next

        return prev


class Solution(object):
    def upsideDownBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        s, tmp = [], root
        while tmp:
            s.append(tmp)
            tmp.left, tmp = None, tmp.left

        for i in reversed(range(1, len(s))):
            #print s[i].val
            s[i].left, s[i].right, s[i-1].right = s[i-1].right, s[i-1], None
        return s[-1
