"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""

class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):  
        # check if empty
        # if empty put node here @ root
        # else if new node < node.value, go left
        #  if >= go right, insert(value)
        if value < self.value:
            if self.left is None:
                self.left = BinarySearchTree(value)
        else: 
            if self.right is None:
                self.right = BinarySearchTree(value)
            else: 
                self.right.insert(value)



    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # at start, self will be root
        # compare target against self
        # 
        # when searching fo False: we know we need to go in 1 direction
        # but there's nothing in the left or right direction

        if target == self.value:
            return True
        if target < self.value:
            # go left
            if not self.left:
                return False
            return self.left.contains(target)

        else:
            # go right
            if not self.right:
                return False
            return self.right.contains(target)


    # Return the maximum value found in the tree
    def get_max(self):
        # if there's a right
        if self.right:
            return self.right.get_max()
        else:
            # return root
            return self.value


    # Call the function `fn` on the value of each node
    def for_each(self, fn):
   

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
