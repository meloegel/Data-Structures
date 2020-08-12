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
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.length = 0

    # Insert the given value into the tree
    # w/ recursion
    # def insert(self, value):
    #     if value < self.value:
    #         if self.left:
    #             self.left.insert(value)
    #         else:
    #             self.left = BSTNode(value)
    #     else:
    #         if self.right:
    #             self.right.insert(value)
    #         else:
    #             self.right = BSTNode(value)
    # w/o recursion
    def insert(self, value):
        current_node = self
        while current_node is not None:
            if value < current_node.value:
                if current_node.left is None:
                    current_node.left = BSTNode(value)
                    current_node.length += 1
                    return
                else:
                    current_node = current_node.left
            else:
                if current_node.right is None:
                    current_node.right = BSTNode(value)
                    current_node.length += 1
                    return
                else:
                    current_node = current_node.right

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        current_node = self
        while current_node is not None:
            if target < current_node.value:
                if current_node.left is None:
                    return False
                else:
                    current_node = current_node.left
            elif target > current_node.value:
                if current_node.right is None:
                    return False
                else:
                    current_node = current_node.right
            else:
                return True

    # Return the maximum value found in the tree
    def get_max(self):
        current_node = self
        while current_node is not None:
            if current_node.right is None:
                return current_node.value
            else:
                current_node = current_node.right

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        if self is None:
            return
        else:
            left_tree = BSTNode.for_each(self.left, fn)
            right_tree = BSTNode.for_each(self.right, fn)
            return fn(self.value)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self):
        pass

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self):
        pass

"""
This code is necessary for testing the `print` methods
"""
bst = BSTNode(1)

bst.insert(8)
bst.insert(5)
bst.insert(7)
bst.insert(6)
bst.insert(3)
bst.insert(4)
bst.insert(2)

bst.bft_print()
bst.dft_print()

# print("elegant methods")
# print("pre order")
# bst.pre_order_dft()
# print("in order")
# bst.in_order_dft()
# print("post order")
# bst.post_order_dft()  
