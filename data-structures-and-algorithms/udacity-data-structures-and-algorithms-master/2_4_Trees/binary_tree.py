class Node(object):
    def __init__(self, value, left=None, right=None):
        self.__value = value
        self.__left = None
        self.__right = None

    def set_value(self, value):
        self.__value = value
    
    def get_value(self):
        return self.__value

    def set_right(self, right):
        self.__right = right
    
    def get_right(self):
        return self.__right

    def has_right(self):
        return self.__right is not None
    
    def set_left(self, left):
        self.__left = left
    
    def get_left(self):
        return self.__left

    def has_left(self):
        return self.__left is not None
    
    def compare(self, other):
        return 1 if self.get_value() > other.get_value() else -1 if self.get_value() < other.get_value() else 0
    
    def __str__(self):
        return str(self.__value)


class Tree(object):
    def __init__(self, initial_value):
        self.__root = Node(initial_value)
    
    def get_root(self):
        return self.__root

    def set_root(self, value):
        self.__root = Node(value)
    
    def insert(self, value):
        new_node = Node(value)
        node = self.get_root()
        if node == None:
            self.set_root(new_node)
            return
        
        while(True):
            pos = new_node.compare(node)
            if pos == 0:
                node.set_value(new_node.get_value())
                break
            elif pos == -1:
                if node.has_left():
                    node = node.get_left()
                else:
                    node.set_left(new_node)
                    break
            else:
                if node.has_right():
                    node = node.get_right()
                else:
                    node.set_right(new_node)
                    break
    
    def search(self, value):
        node = self.get_root()
        target = Node(value)
        
        while(True):
            pos = target.compare(node)
            if pos == 0:
                return True
            elif pos == -1:
                if node.has_left():
                    node = node.get_left()
                else:
                    return False
            else:
                if node.has_right():
                    node = node.get_right()
                else:
                    return False

