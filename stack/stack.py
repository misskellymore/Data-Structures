"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""

from collections import deque

class Stack:
    def __init__(self):
        self.size = 0
        self.storage = [] if storage == None else storage 

    def __len__(self):
        if self.size < 0:
            self.size = 0
        return self.size

    def push(self, value):
        self.size += 1
        return self.storage.append(value)

    def pop(self):
        self.size -= 1
        if len(self.storage) == 0:
            return None
        else: 
            item = self.storage.pop()
            return item


# class Node:
#     def __init__(self, value= None, next_node= None):
#         self.value = value
#         self.next_node = next_node

#     def get_value(self):
#         return self.value 

#     def get_next(self):
#         return self.next_node

#     def set_next(self, new_next):
#         self.next_node = new_next









