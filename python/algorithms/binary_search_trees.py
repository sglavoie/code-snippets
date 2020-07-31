class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

root = Node(2)
root.left = Node(1)
root.right = Node(10)
root.right.left = Node(8)
root.right.right = Node(12)

def tree_search_recursive(node, value):
    if node is None:
        return node
    if value == node.data:
        return node.data
    if value < node.data:
        return tree_search_recursive(node.left, value)
    return tree_search_recursive(node.right, value)

def tree_search_iterative(node, value):
    while node is not None and value != node.data:
        if value < node.data:
            node = node.left
        else:
            node = node.right
    return node
