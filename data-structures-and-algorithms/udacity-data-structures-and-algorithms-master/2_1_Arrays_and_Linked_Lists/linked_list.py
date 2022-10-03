class Node(object):
    def __init__(self, value, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev


class LinkedList:
    def __init__(self, input_list=[]):
        self.__head = None
        self.__tail = None
        self.__size = 0

        for value in input_list:
            self.append(value)
    
    def _get_head(self):
        return self.__head

    def append(self, value):
        if self.__head is None:
            self.__head = Node(value)
            self.__tail = self.__head
        else:
            self.__tail.next = Node(value)
            self.__tail.next.prev = self.__tail
            self.__tail = self.__tail.next
        self.__size += 1
    
    def prepend(self, value):
        if self.__head is None:
            self.__head = Node(value)
            self.__tail =self.__head
        else:
            self.__head.prev = Node(value)
            self.__head.prev.next = self.__head
            self.__head = self.__head.prev
        self.__size += 1
    
    def search(self, value):
        placeholder = self.__head
        while placeholder is not None:
            if placeholder.value == value:
                return placeholder
            placeholder = placeholder.next
        return None
    
    def remove(self, value):
        node = self.search(value)
        if node is None:
            return False
        
        if self.__size == 1:
            self.__head = self.__tail = None
        elif node is self.__head:
            self.__head = self.__head.next
            self.__head.prev = None
        elif node is self.__tail:
            self.__tail = self.__tail.prev
            self.__tail.next = None
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
            node = None
        self.__size -= 1
    
    def pop_left(self):
        if self.__size == 0:
            raise IndexError('List is empty!')
        
        value = self.__head.value
        if self.__size == 1:
            self.__head = self.__tail = None
        else:
            self.__head = self.__head.next
            self.__head.prev = None
        self.__size -= 1
        return value
    
    def pop_right(self):
        if self.__size == 0:
            raise IndexError('List is empty!')
        
        value = self.__tail.value
        if self.__size == 1:
            self.__head = self.__tail = None
        else:
            self.__tail = self.__tail.prev
            self.__tail.next = None
        self.__size -= 1
        return value
    
    def insert(self, value, pos):
        if pos >= self.__size:
            self.append(value)
        elif pos == 0:
            self.prepend(value)
        else:
            placeholder = self.__head
            while pos > 0:
                placeholder = placeholder.next
                pos -= 1
            new_node = Node(value)
            new_node.next = placeholder
            new_node.prev = placeholder.prev
            new_node.prev.next = new_node
            placeholder.prev = new_node
            self.__size += 1
    
    def reverse(self):
        reversed_list = LinkedList()
        placeholder = self.__head
        while placeholder is not None:
            reversed_list.prepend(placeholder.value)
        return reversed_list
    
    def is_circular(self):
        if self.__head is None:
            return False
        
        slow = self.__head
        fast = self.__head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                return True
        return Flase
    
    def size(self):
        return self.__size
    
    def to_list(self):
        output = []
        placeholder = self.__head
        while placeholder is not None:
            output.append(placeholder.value)
            placeholder = placeholder.next
        return output
    
    def __iter__(self):
        placeholder = self.__head
        while placeholder is not None:
            yield placeholder.value
            placeholder = placeholder.next
    
    def __str__(self):
        output = ''
        placeholder = self.__head
        while placeholder is not None:
            output += str(placeholder.value)
            output += ' '
        return output.strip()


if __name__ == '__main__':
    # Test prepend
    linked_list = LinkedList()
    linked_list.prepend(1)
    assert linked_list.to_list() == [1], f"list contents: {linked_list.to_list()}"
    linked_list.append(3)
    linked_list.prepend(2)
    assert linked_list.to_list() == [2, 1, 3], f"list contents: {linked_list.to_list()}"

    # Test append
    linked_list = LinkedList()
    linked_list.append(1)
    assert linked_list.to_list() == [1], f"list contents: {linked_list.to_list()}"
    linked_list.append(3)
    assert linked_list.to_list() == [1, 3], f"list contents: {linked_list.to_list()}"

    # Test search
    linked_list.prepend(2)
    linked_list.prepend(1)
    linked_list.append(4)
    linked_list.append(3)
    assert linked_list.search(1).value == 1, f"list contents: {linked_list.to_list()}"
    assert linked_list.search(4).value == 4, f"list contents: {linked_list.to_list()}"

    # Test remove
    linked_list.remove(1)
    assert linked_list.to_list() == [2, 1, 3, 4, 3], f"list contents: {linked_list.to_list()}"
    linked_list.remove(3)
    assert linked_list.to_list() == [2, 1, 4, 3], f"list contents: {linked_list.to_list()}"
    linked_list.remove(3)
    assert linked_list.to_list() == [2, 1, 4], f"list contents: {linked_list.to_list()}"

    # Test pop
    value = linked_list.pop_left()
    assert value == 2, f"list contents: {linked_list.to_list()}"
    assert linked_list._get_head().value == 1, f"list contents: {linked_list.to_list()}"

    # Test insert
    linked_list.insert(5, 0)
    assert linked_list.to_list() == [5, 1, 4], f"list contents: {linked_list.to_list()}"
    linked_list.insert(2, 1)
    assert linked_list.to_list() == [5, 2, 1, 4], f"list contents: {linked_list.to_list()}"
    linked_list.insert(3, 6)
    assert linked_list.to_list() == [5, 2, 1, 4, 3], f"list contents: {linked_list.to_list()}"

    # Test size
    assert linked_list.size() == 5, f"list contents: {linked_list.to_list()}"