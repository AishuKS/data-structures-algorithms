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

stack = []
stack.append(root)
preorder = []
while stack:
    
    node = stack.pop()
    if node.right:
        stack.append(node.right)
    if node.left:
        stack.append(node.left)
    
    preorder.append(node.data)

print(preorder)