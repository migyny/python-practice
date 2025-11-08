class TreeNode():
     def __init__(self, val, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right


def inorder_traversal(root):

    result = []

    def traverse(current):
        if not current:
            return

        traverse(current.left)
        result.append(current.val)
        traverse(current.right)

    traverse(root)

    return result
