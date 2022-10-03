class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self):
        self.__head = None
        self.__size = 0
    
    def is_empty(self):
        return self.__size == 0
    
    def size(self):
        return self.__size
        
    def push(self, elem):
        node = Node(elem)

        if self.__head is None:
            self.__head = node
        else:
            node.next = self.__head
            self.__head = node
            
        self.__size += 1
    
    def pop(self):
        if self.__size == 0:
            return None

        node = self.__head
        self.__head = node.next
        self.__size -= 1
        return node.value
    
    def top(self):
        if self.__size == 0:
            return None
        return self.__head.value
    
    @staticmethod
    def reverse(stack):
        reverse_stack = Stack()
        while stack.top() is not None:
            reverse_stack.push(stack.pop())
        return reverse_stack


if __name__ == '__main__':
    stack = Stack()
    stack.push(10)
    stack.push(20)
    stack.push(30)
    stack.push(40)
    stack.push(50)

    # Test size
    print ("Pass" if (stack.size() == 5) else "Fail")

    # Test pop
    print ("Pass" if (stack.pop() == 50) else "Fail")

    # Test push
    stack.push(60)
    print ("Pass" if (stack.pop() == 60) else "Fail")
    print ("Pass" if (stack.pop() == 40) else "Fail")
    print ("Pass" if (stack.pop() == 30) else "Fail")
    stack.push(50)
    print ("Pass" if (stack.size() == 3) else "Fail")