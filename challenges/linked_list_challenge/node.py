# Linked List
# A series of nodes that points to another node
# Node holds two pieces of information
# data = information we give it
# 

"""
Schematic for our Unordered List

UnorderedList()         -> creates a new empty unordered list
add(item)               -> adds an item to the list
remove(item)            -> removes the specified item from the list
search(item)            -> searches the list for the item specified
is_empty()              -> Returns if the list is empty or not
length()                -> Returns the length of the list
append(item)            -> Adds an item to the end of the list
index(item)             -> returns the position of the item
insert(position, item)  -> inserts an item in the list at the index
pop()                   -> removes the item at the end of the list
pop(index)              -> removes item at specified index
"""

class Node:                                 # single object in our node

    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return f'{ self.data } -> { self.next}'

    def get_data(self):                     # gets data
        return self.data

    def edit_data(self, new_value):         # to modify existing data with new value
        self.data = new_value
    
    def get_next(self):                     # any self.next node will return itself
        return self.next

    def set_next(self, next_node):
        self.next = next_node
