from collections import deque, defaultdict
class TreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        
# root = TreeNode(1)
# root.left = TreeNode(2)
# root.right = TreeNode(3)
# root.left.left = TreeNode(4)
# root.left.right = TreeNode(5)
# root.right.right = TreeNode(7)
# root.left.right.left = TreeNode(6)

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
# root.left.right = TreeNode(4)
# root.left.right.right = TreeNode(5)
# root.left.right.right.right = TreeNode(6)
# root.left.right.right.right.right = TreeNode(7)

def symmetrical(p,q):
    if not p and not q:
        return False
    if not p or not q:
        return True
    return (p.data == q.data) and symmetrical(p.right, q.left) and symmetrical(p.left, q.right)

p = root
q = root
print(symmetrical(p,q))