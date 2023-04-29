class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


# A function to do inorder tree traversal
def print_inorder(root):
    if root:
        # First recur on left child
        print_inorder(root.left)

        # then print the data of node
        print(root.val),

        # now recur on right child
        print_inorder(root.right)


# A function to do preorder tree traversal
def print_preorder(root):
    if root:
        # First print the data of node
        print(root.val),

        # Then recur on left child
        print_preorder(root.left)

        # Finally recur on right child
        print_preorder(root.right)


# A function to do postorder tree traversal
def print_postorder(root):
    if root:
        # First recur on left child
        print_postorder(root.left)

        # the recur on right child
        print_postorder(root.right)

        # now print the data of node
        print(root.val),


# Driver code
if __name__ == "__main__":
    root = Node(25)
    root.left = Node(15)
    root.left.left = Node(10)
    root.left.left.left = Node(4)
    root.left.left.right = Node(12)
    root.left.right = Node(22)
    root.left.right.left = Node(18)
    root.left.right.right = Node(24)
    root.right = Node(50)
    root.right.left = Node(35)
    root.right.left.left = Node(31)
    root.right.left.right = Node(44)
    root.right.right = Node(70)
    root.right.right.left = Node(66)
    root.right.right.right = Node(90)

    # Function call
    print_preorder(root)
    print("-" * 10)
    print_postorder(root)
    print("-" * 10)
    print_inorder(root)
