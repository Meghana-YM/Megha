'''class node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def dfs_preorder(root):
    if root==None:
        return
    print(root.data)
    dfs_preorder(root.left)
    dfs_preorder(root.right) 
def dfs_postorder(root):
    if root==None:
        return
    dfs_postorder(root.left)
    dfs_postorder(root.right)
    print(root.data) 
                                                                  
root=node(1)
root.left=node(2) 
root.right=node(3)
root.left.left=node(4)
root.left.right=node(5)
print(root.data)
print(root.left.data) 
print(root.right.data)
print(root.left.left.data)
print(root.left.right.data) 
dfs_inorder(root)
dfs_preorder(root)
dfs_postorder(root) ''' 
'''class node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
    def bfs_preorder(root):
        if root==None:
            return
        print(root.data)
        bfs_preorder(root.left)
        bfs_preorder(root.right) 
        q=[4]
        while q:
            a=pop(0)
            print(a.data)
        if a.left:
            q.append(a.left)
        if a.right:
            q.append(a.right)
bfs_preorder(root) '''               
