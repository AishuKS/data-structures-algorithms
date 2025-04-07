class TreeNode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
        
p = TreeNode(1)
p.left = TreeNode(2)
# p.right = TreeNode(3)
  
q = TreeNode(1)
# q.left = TreeNode(2)
q.right = TreeNode(3)


# METHOD 1
def traversal(p,q):
    if not p and not q:
        return True
    
    if not p or not q:
        return False
    
    if p.val != q.val:
        return False
    
    if not traversal(p.left, q.left):
        return False
    
    if not traversal(p.right, q.right):
        return False

    return p.val == q.val and traversal(p.left, q.left) and traversal(p.right, q.right)
    
print(traversal(p,q))

# METHOD 2
# def traversal(p,q):
#     if not p and not q:
#         return True
    
#     if not p or not q:
#         return False

#     return p.val == q.val and traversal(p.left, q.left) and traversal(p.right, q.right)
    
# print(traversal(p,q))