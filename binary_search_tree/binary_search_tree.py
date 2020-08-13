from collections import deque
# from stack import Stack 
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
class Stack:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def __len__(self):
        return self.size

    def push(self, value):
        self.size += 1
        self.storage.add_to_tail(value)
        

    def pop(self):
        if self.size > 0:
            self.size -= 1
            return self.storage.remove_tail()
        return None

        
#Node
class Node:
    def __init__(self, value, next_node = None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value
    
    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next


#LinkedList
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def add_to_tail(self, value):
        new_node = Node(value)
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.set_next(new_node)
            self.tail = new_node

    def remove_tail(self):
        if self.head is None and self.tail is None:
            return None
        if self.head == self.tail:
            val = self.head.get_value()
            self.head = None
            self.tail = None
            return val
        else:
            val = self.tail.get_value()
            current = self.head
            while current.get_next() != self.tail:
                current = current.get_next()
            self.tail = current
            self.tail.set_next(None)
            return val

    def remove_head(self):
        if self.head is None and self.tail is None:
            return None
        if self.head == self.tail:
            val = self.head.get_value()
            self.head = None
            self.tail = None
            return val
        else:
            val = self.head.get_value()
            self.head = self.head.get_next()
            return val

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
        #w/ recursion
        # if not self.right:
        #     return self.value
        # return self.right.get_max()
        #w/o recursion
        current_node = self
        while current_node is not None:
            if current_node.right is None:
                return current_node.value
            else:
                current_node = current_node.right

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        # fn(self.value)
        # if self.left:
        #     self.left.for_each(fn)
        # if self.right:
        #     self.right.for_each(fn)

        # if self is None:
        #     return
        # else:
        #     left_tree = BSTNode.for_each(self.left, fn)
        #     right_tree = BSTNode.for_each(self.right, fn)
        #     return fn(self.value)

        #depth-first itertative
        # stack = []
        # stack.append(self)
        # while len(stack) > 0:
        #     current_node = stack.pop()
        #     if current_node.right:
        #         stack.append(current_node.right)
        #     if current_node.left:
        #         stack.append(current_node.left)

        #     fn(current_node.value)

        #breadth-frist traversal
        
        q = deque()
        q.append(self)

        while len(q) > 0:
            current_node = q.popleft()
            if current_node.left:
                q.append(current_node.left)
            if current_node.right:
                q.append(current_node.right)

            fn(current_node.value)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if node.left:
            self.in_order_print(node.left)
        print(node.value)
        if node.right:
            self.in_order_print(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        q = deque()
        q.append(node)

        while len(q) > 0:
            current = q.popleft()
            print(current.value)
            if current.left:
                q.append(current.left)
            if current.right:
                q.append(current.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        stack = Stack()
        stack.push(node)
        while stack.size != 0:
            node = stack.pop()
            print(node.value)
            if node.right:
                stack.push(node.right)
            if node.left:
                stack.push(node.left)


    # Stretch Goals -------------------------
    # Note: Research may be required

    # # Print Pre-order recursive DFT
    def pre_order_print(self):
        if not self:
            return
        print(self.value)
        if self.left:
            self.left.pre_order_print()
        if self.right:
            self.right.pre_order_print()

    # # Print Post-order recursive DFT
    def post_order_print(self):
        if not self:
            return
        if self.left:
            self.left.post_order_print()
        if self.right:
            self.right.post_order_print()
        print(self.value)

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

bst.bft_print(bst)
bst.dft_print(bst)

print("elegant methods")
print("pre order")
bst.pre_order_print()
print("in order")
bst.in_order_print(bst)
print("post order")
bst.post_order_print()  