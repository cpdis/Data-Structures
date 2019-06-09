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
        # check the case if the current value is equal to the target
        if target == self.value:
            return True
            # check to the right
        elif target > self.value:
            # if there's nothing to the right then return false, otherwise
            # recursively search for the target
            if not self.right:
                return False
            else:
                self.right.contains(target)
        elif target < self.value:
            # if there's nothing to the left then return false, otherwise
            # recursively search for the target
            if not self.left:
                return False
            else:
                if self.left is not None:
                    if self.left.contains(target):
                        return True
                if self.right is not None:
                    if self.right.contains(target):
                        return True

    def get_max(self):
        if self.right is None:
            return self.value
        else:
            return self.right.get_max()

    def for_each(self, cb):
        cb(self.value)

        if self.right is None and self.left is None:
            return
        else:
            if self.left is not None:
                self.left.for_each(cb)
            if self.right is not None:
                self.right.for_each(cb)
        return


new_tree = BinarySearchTree(15)
new_tree.insert(3)
new_tree.insert(0)
new_tree.insert(13)
new_tree.insert(20)
new_tree.insert(-3)
new_tree.insert(73)

print(new_tree.contains(1))
