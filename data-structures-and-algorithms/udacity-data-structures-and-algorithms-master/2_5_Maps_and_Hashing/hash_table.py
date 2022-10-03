class HashTable(object):
    def __init__(self):
        self.__table = [None] * 10000

    def store(self, string):
        hash_value = self.hash(string)
        if self.__table[hash_value] != None:
            self.__table[hash_value].append(string)
        else:
            self.__table[hash_value] = [string]

    def lookup(self, string):
        hash_value = self.hash(string)
        if self.__table[hash_value] != None:
            if string in self.__table[hash_value]:
                return hash_value
        return -1

    def hash(self, string):
        return ord(string[0]) * 100 + ord(string[1])


if __name__ == '__main__':
    hash_table = HashTable()
    print (hash_table.hash('UDACITY'))
    print (hash_table.lookup('UDACITY'))
    hash_table.store('UDACITY')
    print (hash_table.lookup('UDACITY'))
    hash_table.store('UDACIOUS')
    print (hash_table.lookup('UDACIOUS'))
