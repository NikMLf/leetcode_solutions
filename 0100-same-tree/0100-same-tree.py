# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def f(node_1, node_2):
            if node_1 is None and node_2 is None:
                return True
            else:
                if node_1 is None or node_2 is None:
                    return False
                if node_1.val == node_2.val:
                    return True
                return False
        
        def f_(tree_left, tree_right):
            if f(tree_left, tree_right):
                if (tree_left is not None and tree_right is not None) and (tree_left is not None and tree_right is not None):
                    return f_(tree_left.left, tree_right.left) and f_(tree_left.right, tree_right.right)
                elif (tree_left is None and tree_right is None):
                    return True
                else:
                    return False
            else:
                return False
        return f_(p, q)