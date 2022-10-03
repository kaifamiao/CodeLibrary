class Queue:
    def __init__(self, initial_size: int= 10):
        self.__queue = [0 for _ in range(initial_size)]
        self.__head = -1
        self.__tail = 0
        self.__size = 0
    
    def size(self):
        return self.__size
    
    def is_empty(self):
        return self.__size == 0
    
    def enqueue(self, elem):
        if self.__size == len(self.__queue):
            self._resize()

        self.__queue[self.__tail] = elem
        self.__size += 1
        self.__tail = (self.__tail + 1) % len(self.__queue)
        if self.__head == -1:
            self.__head = 0
    
    def front(self):
        if self.__head == -1:
            return None
        else:
            return self.__queue[self.__head]
    
    def dequeue(self):
        if self.is_empty():
            self.__head = -1
            self.__tail = 0
            return None
        
        value = self.__queue[self.__head]
        self.__head = (self.__head + 1) % len(self.__queue)
        self.__size -= 1
        return value
    
    def _resize(self):
        new_queue = [0 for _ in range(len(self.__queue) * 2)]
        new_index = 0
        for i in range(self.__size):
            new_queue[new_index] = self.__queue[self.__head]
            self.__head = (self.__head + 1) % len(self.__queue)
            new_index += 1
        self.__head = 0
        self.__tail = index


if __name__ == '__main__':
    # Setup
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)

    # Test size
    print ("Pass" if (q.size() == 3) else "Fail")

    # Test dequeue
    print ("Pass" if (q.dequeue() == 1) else "Fail")

    # Test enqueue
    q.enqueue(4)
    print ("Pass" if (q.dequeue() == 2) else "Fail")
    print ("Pass" if (q.dequeue() == 3) else "Fail")
    print ("Pass" if (q.dequeue() == 4) else "Fail")
    q.enqueue(5)
    print ("Pass" if (q.size() == 1) else "Fail")
