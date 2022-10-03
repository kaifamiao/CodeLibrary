class Node(object):
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashMap(object):
    def __init__(self, capacity=10):
        self.__buckets = [None for _ in range(capacity)]
        self.__prime = 37
        self.__load_factor = 0.7
        self.__size = 0

    def put(self, key, value):
        index = self.__hash(key)
        new_node = Node(key, value)
        root = self.__buckets[index]

        while root is not None:
            if root.key == key:
                root.value = value
                return
            root = root.next
        
        root = self.__buckets[index]
        new_node.next = root
        self.__buckets[index] = new_node
        self.__size += 1

        load_factor = self.__size / len(self.__buckets)
        if load_factor > 0.7:
            self.__size = 0
            self.__rehash()

    def get(self, key):
        index = self.__hash(key)
        root = self.__buckets[index]
        while root is not None:
            if root.key == key:
                return root.value
            root = root.next
        return None

    def size(self):
        return self.__size

    def index(self, key):
        return self.__hash(key)

    def __hash(self, string):
        key = str(string)
        hash_code = 0
        coef = 1
        n = len(self.__buckets)

        for char in string:
            hash_code += ord(char) * coef
            hash_code %= n
            coef *= self.__prime
        
        return hash_code % n
    
    def __rehash(self):
        old_n = len(self.__buckets)
        old_buckets = self.__buckets
        new_num = 2 * old_n
        self.__buckets = [None for _ in range(new_num)]

        for root in old_buckets:
            while root is not None:
                key = root.key
                value = root.value
                self.put(key, value)
                head = head.next

    def delete(self, key):
        index = self.index(key)
        root = self.__buckets[index]

        previous_node = None
        while root is not None:
            if root.key == key:
                if previous_node is None:
                    self.__buckets[index] = root.next
                else:
                    previous_node.next = root.next
                self.__size -= 1
                return
            else:
                previous_node = root
                root = root.next

if __name__ == '__main__':
    hash_map = HashMap(7)
    hash_map.put("one", 1)
    hash_map.put("two", 2)
    hash_map.put("three", 3)
    hash_map.put("neo", 11)

    print("size: {}".format(hash_map.size()))


    print("one: {}".format(hash_map.get("one")))
    print("neo: {}".format(hash_map.get("neo")))
    print("three: {}".format(hash_map.get("three")))
    print("size: {}".format(hash_map.size()))

    hash_map.delete("one")

    print(hash_map.get("one"))
    print(hash_map.size())
