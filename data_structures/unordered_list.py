from node import Node

class UnorderedList:
    
    def __init__(self):             # doesn't take anything for now
        self.head = None

    def add_item(self, new_item):
        temp = Node(new_item)
        temp.set_next(self.head)    # because Node is None
        self.head = temp
    
    def is_empty(self):
        return self.head == None    #

    def length(self):
        count = 0
        current = self.head

        while current != None:
            count += 1
            current = current.get_next()
        return count

    def remove(self, item):
        current = self.head
        previous = None
        found = False

        while not found:
            if current.get_data() == item:
                found = True
            else:
                previous = current
                current = current.get_next()
        
        if previous == None:
            self.head == current.get_next()
        else:
            previous.set_next(current.get_next())
        return current

    def search(self, item):
        current = self.head
        found = False

        while current != None and not found:
            if current.get_data() == item:
                found = True
            else:
                current = current.get_next()
        return found

    def index(self, item):
        index = 0
        current = self.head
        found = False

        while current != None and not found:
            if current.get_data == item:
                found = True
        else:
            current = current.get_next()
            index += 1
        return index
        

    
my_linked = UnorderedList()
my_linked.add_item(89)
my_linked.add_item("Hello")

print(my_linked.length())

my_linked.remove(89)

print(my_linked.length())

print(my_linked.search("Hell"))