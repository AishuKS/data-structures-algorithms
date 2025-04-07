from collections import deque
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

def levelOrder(root):
    if not root:
        return
    left_to_right = True
    while q:
        level = []
        n = len(q)
        for i in range(n):
            node = q.popleft()
            if left_to_right:
                level.append(node.data)
            else:
                level.insert(0, node.data)
            
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        left_to_right = not left_to_right
        answer.append(level)

q = deque()
q.append(root)
answer = []
levelOrder(root)
print(answer)