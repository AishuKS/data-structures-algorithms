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

def findPath(root, ds, ans):
    if not root:
        return
    ds.append(root.data)
    if not root.left and not root.right:
        ans.append(ds[:])
    else:
        findPath(root.left, ds, ans)
        findPath(root.right, ds, ans)
    ds.pop()
    

ans = []
ds = []
findPath(root, ds, ans)
print(ans)