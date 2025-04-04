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

def balancedBinaryTree(root):
    if not root:
        return 0

    lh = balancedBinaryTree(root.left)
    if lh == -1:
        return -1
    rh = balancedBinaryTree(root.right)
    if rh == -1:
        return -1
    
    if abs(lh - rh) > 1:
        return -1
    
    return max(lh,rh) + 1

if balancedBinaryTree(root) == -1:
    print("Not Balanced")

else:
    print("Balanced")
