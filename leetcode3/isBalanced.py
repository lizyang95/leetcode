class Solution(object):
    def depth(self,root):
        if root == None:
            return 0
        return max(self.depth(root.left),self.depth(root.right))+1

    def isBalanced(self,root):
        if root == None:
            return True
        leftheight = self.depth(root.left)
        rightheight = self.depth(root.right)

        return abs(leftheight-rightheight)<=1 and self.isBalanced(root.left) and self.isBalanced(root.right)


class Solution_DFS(object):
    def dfsHeight(self,root):
        if root == None:
            return 0

        leftheight = self.dfsHeight(root.left)
        if leftheight == -1:
            return -1

        rightheight = self.dfsHeight(root.right)
        if rightheight == -1:
            return -1

        if abs(leftheight-rightheight)>1:
            return -1

        return max(leftheight,rightheight)+1

    def isBalanced(self,root):
        return self.dfsHeight(root) != -1
