from collections import deque, defaultdict
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


node = defaultdict(lambda: defaultdict(set))
q = deque([(root, (0, 0))])

while q:
    temp, (x,y) = q.popleft()
    node[x][y].add(temp.data)
    if temp.left:
        q.append((temp.left,(x-1,y+1)))
    if temp.right:
        q.append((temp.right,(x+1,y+1)))
    
ans = []
for x in sorted(node.keys()):
    ds = []
    for y in sorted(node[x].keys()):
        ds.extend(sorted(node[x][y]))
    ans.append(ds)
print(ans)