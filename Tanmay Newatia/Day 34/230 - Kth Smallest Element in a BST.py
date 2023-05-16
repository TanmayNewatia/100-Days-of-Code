# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.arr=[]
        self.preorder(root)
        self.arr.sort()
        return self.arr[k-1]

    def preorder(self,root):
        if(root):
            self.arr+=[root.val]
            self.preorder(root.left)
            self.preorder(root.right)
        