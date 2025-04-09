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

q = deque()
q.append(root)
rightView = []
leftView = []
while q:
    level = []
    count = 0
    for i in range(len(q)):
        
        node = q.popleft()
        if count == 0:
            leftView.append(node.data)
            count = 1
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)
    rightView.append(node.data)

print(rightView)
print(leftView)