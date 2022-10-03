class Node(object):
    def __init__(self, key):
        self.key = key
        self.next = None
        self.prev = None


class LinkedList(object):
    """
    A doubly linked list that is used in LRUCache to keep track of the order in
    which keys were inserted. It only needs to insert new keys at the front of the
    list and remove least recently inserted keys from the end of the list.
    """
    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__size = 0
    
    def size(self):
        return self.__size
    
    def prepend(self, key):
        node = self.__head
        new_node = Node(key)

        if node is None:
            self.__head = self.__tail = new_node
        else:
            self.__head = new_node
            self.__head.next = node
            node.prev = self.__head
        
        self.__size += 1
    
    def pop(self):
        if self.__size == 0:
            return None
        
        last_node = self.__tail
        self.__tail = last_node.prev
        self.__tail.next = None
        self.__size -= 1
        return last_node.key


class LRUCache(object):
    """
    LRUCache keeps a maximum given number of key-value pairs at any point in time.
    When the capacity is reached, it removes the least recently inserted key from
    the cache.

    LRU or Least Recently Used cache uses python dictionary to save key-value
    pairs. At the same time, it keeps a doubly linked list of keys to keep
    track of the order of the key insertions. Similar behavior can be achieved 
    by using python's ordered dictionary.
    """
    def __init__(self, capacity):
        self.__capacity = capacity
        self.__list = LinkedList()
        self.__dict = dict()

    def get(self, key):
        return self.__dict[key] if key in self.__dict else -1

    def set(self, key, value):
        if key in self.__dict:
            return
        if self.__capacity == self.__list.size():
            del self.__dict[self.__list.pop()]
        
        self.__list.prepend(key)
        self.__dict[key] = value


if __name__ == '__main__':
    our_cache = LRUCache(5)
    our_cache.set(1, 1)
    our_cache.set(2, 2)
    our_cache.set(3, 3)
    our_cache.set(5, "Not a number")
    our_cache.set(None, 42)


    print(our_cache.get(1))
    # returns 1
    print(our_cache.get(2))
    # returns 2
    print(our_cache.get(4))
    # returns -1
    print(our_cache.get(5))
    # returns "Not a number"
    print(our_cache.get(6))
    # returns -1