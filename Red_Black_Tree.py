class RBNode:
    def __init__(self, key):
        self.key = key
        self.color = 'red'
        self.left = None
        self.right = None
        self.parent = None


class RedBlackTree:
    def __init__(self):
        self.NULL_LEAF = RBNode(None)
        self.NULL_LEAF.color = 'black'
        self.root = self.NULL_LEAF

    def insert(self, key):
        """Insert a node into the tree (keeps only the insertion step).

        Note: This version retains the insertion logic but omits
        rebalancing (fix-up) and rotation methods. It intentionally
        removes other methods per request and leaves only the
        insertion functionality.
        """
        new_node = RBNode(key)
        new_node.left = self.NULL_LEAF
        new_node.right = self.NULL_LEAF

        parent = None
        current = self.root

        while current != self.NULL_LEAF:
            parent = current
            if new_node.key < current.key:
                current = current.left
            else:
                current = current.right

        new_node.parent = parent

        if parent is None:
            self.root = new_node
        elif new_node.key < parent.key:
            parent.left = new_node
        else:
            parent.right = new_node

        new_node.color = 'red'
