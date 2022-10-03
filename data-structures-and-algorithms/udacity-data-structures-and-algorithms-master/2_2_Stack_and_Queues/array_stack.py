class Stack:
    def __init__(self, initial_size=10):
        self._stack = [0 for _ in range(initial_size)]
        self._index = 0
    
    def is_empty(self):
        return self._index == 0
    
    def size(self):
        return self._index
    
    def push(self, elem):
        if self._index == len(self._stack):
            self._resize()

        self._stack[self._index] = elem
        self._index += 1
    
    def pop(self):
        if self.is_empty():
            return None
        self._index -= 1
        return self._stack[self._index]
    
    def _resize(self):
        new_stack = [0 for _ in range(len(self._stack) * 2)]
        for i, elem in enumerate(self._stack):
            new_stack[i] = elem
        self._stack = new_stack
    
if __name__ == '__main__':
    foo = Stack()
    foo.push(1)
    foo.push(2)
    foo.push(3)
    foo.push(4)
    foo.push(5)
    foo.push(6)
    foo.push(7)
    foo.push(8)
    foo.push(9)
    foo.push(10) # The array is now at capacity!
    foo.push(11) # This one should cause the array to increase in size
    print(foo._stack) # Let's see what the array looks like now!
    print("Pass" if len(foo._stack) == 20 else "Fail") # If we successfully doubled the array size, it should now be 20.

    foo = Stack()
    foo.push("Test") # We first have to push an item so that we'll have something to pop
    print(foo.pop()) # Should return the popped item, which is "Test"
    print(foo.pop()) # Should return None, since there's nothing left in the stack