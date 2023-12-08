# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:

      res = []

      def preorder(root):
        if not root: #if root is empty
          return 

        res.append("(")
        res.append(str(root.val))

        if not root.left and root.right: #there is not left subtree and there is right subtree
          res.append("()")
        preorder(root.left)
        preorder(root.right)
        res.append(")")
      
      preorder(root)
      return "".join(res)[1:-1]#removing the starting and ending brackets