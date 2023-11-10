class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def leaf_node_sum(root):
    if root is None:
        return 0

    if root.left is None and root.right is None:
        return root.key

    return leaf_node_sum(root.left) + leaf_node_sum(root.right)

# Example usage:
# Constructing a sample binary tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

result_sum = leaf_node_sum(root)
print(f"The sum of leaf nodes in the tree is: {result_sum}")
