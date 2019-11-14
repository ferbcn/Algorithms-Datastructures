# Example of a BST (binary search tree) implemented in Python3
# Author: ferbcn

import random
import time

class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.data = value

class Tree:
    def __init__(self):
        self.root = None
        self.sorted_data = []

    def add_node(self, node, value):
        if node == None:
            self.root = Node(value)
        else:
            if value < node.data:
                if node.left == None:
                    node.left = Node(value)
                else:
                    self.add_node(node.left, value)
            else:
                if node.right == None:
                    node.right = Node(value)
                else:
                    self.add_node(node.right, value)

    # print BST in order (sorted list in none descending order)
    def print_in_order(self, node):
        if node != None:
            self.print_in_order(node.left)
            print(node.data)
            self.print_in_order(node.right)

    # returns a new list by traversing the BST in order (returns a sorted list in none descending order)
    def get_in_order(self, node):
        if node != None:
            self.get_in_order(node.left)
            self.sorted_data.append(node.data)
            self.get_in_order(node.right)


if __name__ == "__main__":

    # create random data
    node_count = 10000
    data_range = 1000
    data = [random.randint(-data_range, data_range) for _ in range(node_count)]
    #print(data)

    # sort using BST
    init_time = time.time()
    # build BST adding every data point with time complexity O(n)=log(n)
    myTree = Tree()
    for item in data:
        myTree.add_node(myTree.root, item)
    #traverse BST inorder with average time complexity O(n)=n*log(n)
    myTree.get_in_order(myTree.root)
    #print(myTree.sorted_data)
    #myTree.print_in_order(myTree.root)
    print(f"Sorting using a BST: {time.time()-init_time} sec.")

    # sort using Python's built in sort method (highly efficient at least x50)
    init_time = time.time()
    data.sort()
    #print(data)
    print(f"Sorting using built-in method: {time.time()-init_time} sec.")
