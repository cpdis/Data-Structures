class BinarySearchTree:
    def __init__(self, value):
        # the value of the node we're currently at
        self.value = value
        # the current node's left child
        self.left = None
        # the current node's right child
        self.right = None

    def insert(self, value):
        # check to see if the new node is less than the current node
        if value < self.value:
            # if there's not left child, then place the new node here
            if not self.left:
                self.left = BinarySearchTree(value)
            else:
                # recursively keeps going until it finds a place for
                # the new node
                self.left.insert(value)
        # check to see if the new node is greater than the current node
        elif value >= self.value:
            # if there's no right child, then place the new node here
            if not self.right:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)

    def contains(self, target):
        pass

    def get_max(self):
        if self.right is None:
            return self.value
        else:
            return self.right.get_max()

    def for_each(self, cb):
        pass

