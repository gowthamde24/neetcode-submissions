# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        self.res = float('-inf')
        def getmaxgain(node):
            if not node:
                return 0
            left_gain = max(getmaxgain(node.left),0)
            right_gain = max(getmaxgain(node.right),0)

            current_path = node.val + left_gain + right_gain

            self.res = max(self.res,current_path)

            return node.val + max(left_gain,right_gain)

        getmaxgain(root)
        return self.res
    #     def dfs(root):
    #         nonlocal res
    #         if not root:
    #             return 
    #         left = self.getmax(root.left)
    #         right = self.getmax(root.right)
    #         res = max(res,root.val + left + right)

    #         dfs(root.left)
    #         dfs(root.right)
    #     dfs(root)
    #     return res



    # def getmax(self, root: Optional[TreeNode]) -> int:
    #     if not root:
    #         return 0

    #     left = self.getmax(root.left)
    #     right = self.getmax(root.right)
    #     path = root.val + max (left , right)

    #     return max(0,path)
            
        

        