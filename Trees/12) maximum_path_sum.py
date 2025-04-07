class TreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)
def value(root):
    maxValue = float('-inf')
    def maxSumPath(root):
        nonlocal maxValue
        if not root:
            return 0
        
        lh = max(0, maxSumPath(root.left))
        rh = max(0, maxSumPath(root.right))
        
        maxValue = max(maxValue, root.data+lh+rh)

        return root.data + max(0, lh,rh)


    maxSumPath(root)
    return maxValue
print(value(root))
