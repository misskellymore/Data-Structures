class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next

    def set_next(self, new_next):
        # set this new node's reference to the next node
        self.next = new_next


class LinkedList:
    def __init__(self):
        # what attributes do we need?
        self.head = None
        self.tail = None

    def add_to_head(self, value):
        # TODO time permitting

        # create node
        new_node = Node(value, None)

        if self.head is None:
            self.head = new_node
            self.tail = new_node

        else:
            # prepend
            self.head.set_next(new_node)
            self.head = new_node
            
            
    def add_to_tail(self, value):
        
        new_node = Node(value, None)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.set_next(new_node)
            self.tail = new_node

    def remove_head(self):
        if self.head is None:
            return None

        if not self.head.get_next():
            # pointer
            head = self.head
            self.head = None
            self.tail = None
            return head.get_value()
        value = self.head.get_value()
        self.head = self.head.get_next()
        return value

    def remove_tail(self):
        if self.head is None:
            return None

        # pointer
        cur = self.head

        if self.head is self.tail:
            value = self.head.get_value()
            self.head = None
            self.tail = None
            return value

        while cur.get_next() is not self.tail():
            cur = cur.get_next()

        value = self.tail.get_value()
        self.tail = cur
        self.tail.set_next(None)
        return value


    def contains(self, value):
        if self.head is None:
            return False

        cur = self.head

        while cur is not None:
            if cur.get_value() == value:
                return True
            cur = cur.get_next()
        return False

    def get_max(self):
        if self.head is None:
            return None
        
        max_value = self.head.get_value()
        cur = self.head.get_next()

        while cur:
            if cur.get_value() > max_value:
                max_value = cur.get_value()
            cur = cur.get_next()
        return max_value
