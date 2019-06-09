"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
  after this node. Note that this node could already
  have a next node it is point to."""

    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
  before this node. Note that this node could already
  have a previous node it is point to."""

    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
  accordingly, effectively deleting this ListNode."""

    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    def add_to_head(self, value):
        new_node = ListNode(value)
        self.length += 1

        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            self.head.insert_before(value)
            self.head = self.head.prev

    def remove_from_head(self):
        prev_head = self.head

        if self.length == 0:
            return
        else:
            new_head = self.head.next
            self.head.delete()
            self.head = new_head

            if self.head is not None:
                self.tail = self.tail
            else:
                self.tail = None

            self.length -= 1

        if prev_head is not None:
            return prev_head.value
        else:
            return prev_head

    def add_to_tail(self, value):
        new_node = ListNode(value, None, None)
        self.length += 1

        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def remove_from_tail(self):
        self.length -= 1

        if not self.tail and not self.head:  # if there is no tail
            return None

        if self.head == self.tail:  # if the head = tail, then both = None
            current_tail = self.tail
            self.head = None
            self.tail = None
            return current_tail.value
        else:
            current_tail = self.tail
            self.tail = self.tail.prev
            self.tail.next = None
            return current_tail.value

    def move_to_front(self, node):
        # check to see if it's already in front
        if self.head is not node:
            if node.next and node.prev:
                node.delete()
            current_head = self.head
            self.head = node
            node.next = current_head
            current_head.prev = node

    def move_to_end(self, node):
        if self.length > 1 and node != self.tail:
            current_node = node
            node.delete()
            self.tail.insert_after(current_node.value)
            self.tail = self.tail.next

            if node != self.head:
                self.head = self.head
            else:
                self.head = current_node.next

    def delete(self, node):
        self.length -= 1

        if not self.head and not self.tail:
            return
        if self.head == self.tail:
            self.head = None
            self.tail = None
        elif self.head == node:
            self.head = node.next
            node.delete()
        elif self.tail == node:
            self.tail = node.prev
            node.delete()
        else:
            node.delete()

    def get_max(self):
        current = self.head
        max = 0

        if not self.head:
            return None
        elif self.head == self.tail:
            return self.head.value

        while current:
            if current.value > max:
                max = current.value
            current = current.next

        return max

