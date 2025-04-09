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

q = deque([(root, 0)])
ans = []
map = {}

while q:
    node, line = q.popleft()
    if line not in map:
        map[line] = [node.data]
    else:
        map[line].append(node.data)
    
    if node.left:
        q.append((node.left, line - 1))
    
    if node.right:
        q.append((node.right, line + 1))
    
for keys in sorted(map.items()):
    ans.append(keys[1][-1])
