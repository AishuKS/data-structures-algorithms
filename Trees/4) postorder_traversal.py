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

#preorder traversal
def postorder(root):
    if root is None:
        return
    
    postorder(root.left)      
    postorder(root.right)     
    answer.append(root.data)

answer = []
postorder(root)
print(answer)