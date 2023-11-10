class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def spinal_order_traversal(root):
    if root is None:
        return []

    result = []
    current_level = [root]
    left_to_right = True

    while current_level:
        current_values = []
        next_level = []

        for node in current_level:
            current_values.append(node.key)

            if node.left:
                next_level.append(node.left)
            if node.right:
                next_level.append(node.right)

        if not left_to_right:
            current_values = current_values[::-1]

        result.extend(current_values)
        current_level = next_level
        left_to_right = not left_to_right

    return result

# Example usage:
# Constructing a sample binary tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

result_spinal_order = spinal_order_traversal(root)
print(f"The spinal order traversal of the tree is: {result_spinal_order}")
