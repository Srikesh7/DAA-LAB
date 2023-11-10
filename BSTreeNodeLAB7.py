class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def search_node(root, target):
    if root is None or root.key == target:
        return root

    # Recur down the tree
    if target < root.key:
        return search_node(root.left, target)
    else:
        return search_node(root.right, target)

# Example usage:
# Constructing a sample Binary Search Tree
bst_root = TreeNode(10)
bst_root.left = TreeNode(5)
bst_root.right = TreeNode(15)
bst_root.left.left = TreeNode(3)
bst_root.left.right = TreeNode(7)
bst_root.right.right = TreeNode(20)

target_key = 7
result_node = search_node(bst_root, target_key)

if result_node:
    print(f"Node with key {target_key} found in the Binary Search Tree.")
else:
    print(f"Node with key {target_key} not found in the Binary Search Tree.")
