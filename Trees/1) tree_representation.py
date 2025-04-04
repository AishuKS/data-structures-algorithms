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

def print_tree(root):
    if root is None:
        return
    print(root.data, end=" ")  
    print_tree(root.left)      
    print_tree(root.right)     

# Calling the function to print the tree
print_tree(root)