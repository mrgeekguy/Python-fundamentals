# Binary Tree Data Structure

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def set_value(self, new_value):
        self.value = new_value

    def set_left(self, node):
        self.left = node

    def set_right(self, node):
        self.right = node

    def get_value(self):
        return self.value

    def get_right(self):
        return self.right
    
    def get_left(self):
        return self.left

class BinaryTree:
    def __init__(self, root_node = None):
        self.root_node = root_node
    
    def set_root(self, new_root):
        self.root_node = new_root

    def _post_order(self, node):
        if node:
            return 1 + self._post_order(node.get_left()) + self._post_order(node.get_right())
    
    def length(self):
        return self._post_order(self.root_node)


    def add_node(self, item):
        new_node = TreeNode(item)
        if self.root_node == None:
            self.root_node = new_node
        else:
            position = self._post_order(self.root_node)
            backtrack = []
            right = 0
            left = 1

            start = self.root_node
            
            while position > 0:
                if position % 2 == 0:
                    backtrack.append(right)
                else:
                    backtrack.append(left)
                position = int((position - 1) / 2)

            final = backtrack.pop()
            
            for command in backtrack:
                if command:
                    # left will be true
                    start - start.get_left()
                else:
                    # right will be true
                    start = start.get_right()
            
            if final:
                start.set_left(new_node)
            else:
                start.set_right(new_node)

new_tree = BinaryTree()

new_tree.add_node("finally")
new_tree.add_node("another")
new_tree.add_node("answer")