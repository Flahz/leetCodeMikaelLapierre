class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val  # Value of the node
        self.left = left  # Left child (another TreeNode or None)
        self.right = right  # Right child (another TreeNode or None)

    def diameterOfBinaryTree(self, root):
        
