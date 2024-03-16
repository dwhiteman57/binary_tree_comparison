class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def are_identical(root1, root2):
    if not root1 and not root2:
        return True
    if root1 and root2:
        return (root1.value == root2.value) and \
               are_identical(root1.left, root2.left) and \
               are_identical(root1.right, root2.right)
    return False

# Example Usage
tree1 = TreeNode(1, TreeNode(2), TreeNode(3))
tree2 = TreeNode(1, TreeNode(2), TreeNode(5))
print(are_identical(tree1, tree2))  # Output: True or False
