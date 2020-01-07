# Challenge
# Write an algorithm that removes duplicate entries from a linked list
"""
Start with head
Check if subsequent values are equal
If equal:
    remove duplicate
Otherwise:
    move on
"""

from unordered_list import UnorderedList

def remove_dups(linked_list):
    start = linked_list.head
    previous = None

    while start:
        my_next = start.get_next()                              # moves to the 2nd part of LL

        while my_next:
            if start.get_data() == my_next.get_data():
                previous.set_next(my_next.get_next())              # this moves next past the one we're deleting
            previous = my_next
            my_next = my_next.get_next()
        
        start = start.get_next()

my_list = UnorderedList()
somestuff = [4, 2, 44, 2, 3, 4, 9]

for i in somestuff:
    my_list.add_item(i)

print(my_list)
remove_dups(my_list)
print(my_list)

