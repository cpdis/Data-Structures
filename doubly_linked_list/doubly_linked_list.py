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
        current_head = self.head
        if not current_head:
            self.head = ListNode(value)
        else:
            current_head.insert_before(value)
            self.head = current_head.prev

    def remove_from_head(self):
        if not self.head:
            return None
        else:
            head = self.head
            self.head.delete()
            return head.value

    def add_to_tail(self, value):
        current_tail = self.tail
        if not current_tail:
            new_node = ListNode(value)
            self.head = new_node
            self.tail = new_node
        else:
            current_tail.insert_after(value)
            self.tail = current_tail.next

    def remove_from_tail(self):
        if not self.tail:  # if there is no tail
            return None
        if not self.tail.prev:  # if the head = tail, then both = None
            tail = self.tail
            self.head = None
            self.tail = None
            return tail.value
        else:
            tail = self.tail
            self.tail.delete()
            self.tail = self.tail.prev
            return tail.value

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
        # check to see if it's already in front
        if self.tail is not node:
            if node.next and node.prev:
                node.delete()
            current_tail = self.tail
            self.tail = node
            node.next = current_tail
            current_tail.prev = node

    def delete(self, node):
        if node.next is None and node.prev is not None:
              node.prev.next = None
              self.tail = node.prev
              return node.value
        if node.prev is None and node.next is not None:
              node.next.prev = None
              self.head = node.next
              return node.value
        if node.prev is None and node.next is None:
              self.head = None
              self.tail = None
              return node.value
        else:
              node.delete()
              if node == self.head:
                    self.head = node.next
              if node == self.tail:
                    self.tail = node.prev
        return node.value

    def get_max(self):
        pass

