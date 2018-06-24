# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param inorder, a list of integers
    # @param postorder, a list of integers
    # @return a tree node
    def buildTree(self,inorder,postorder):
        if not inorder:
            return
        root = TreeNode(postorder.pop())
        mid = inorder.index(root.val)
        root.right = self.buildTree(inorder[mid+1:],postorder)
        root.left = self.buildTree(inorder[:mid],postorder)
        return root


class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if inorder:
            ind = inorder.index(preorder.pop(0))
            root = TreeNode(inorder[ind])
            root.left = self.buildTree(preorder, inorder[0:ind])
            root.right = self.buildTree(preorder, inorder[ind+1:])
            return root

            
    def buildTree_dfs(self,preorder,inorder):
        if not preorder: return []

        stack=[]

        preorder=preorder[::-1]
        inorder=inorder[::-1]


        head=TreeNode(preorder.pop())
        stack.append(head)

        while stack:
            if stack[-1].val!=inorder[-1]:
                new=TreeNode(preorder.pop())
                stack[-1].left=new
                stack.append(new)
            if stack[-1].val==inorder[-1]:
                cur=stack.pop()
                inorder.pop()
                if not inorder:
                    break
                if (not stack) or inorder[-1]!=stack[-1].val:
                    new=TreeNode(preorder.pop())
                    cur.right=new
                    stack.append(new)

        return head
