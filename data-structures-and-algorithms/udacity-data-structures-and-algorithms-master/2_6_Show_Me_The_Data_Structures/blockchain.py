import hashlib
import time


class Block:
    def __init__(self, timestamp, data, previous_hash=None):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()

    def calc_hash(self):
        sha = hashlib.sha256()
        sha.update(self.data.encode('utf-8'))
        return sha.hexdigest()
    
    def __str__(self):
        return 'Block is:\nData:{}\nTimestamp:{}\nHash:{}'.format(self.data, self.timestamp, self.hash)


class BlockChain(object):
    def __init__(self):
        self.__head = None
        self.__size = 0
    
    def size(self):
        return self.__size
    
    def append(self, data):
        if self.__head == None:
            self.__head = Block(time.time(), data)
        else:
            self.__head = Block(time.time(), data, self.__head)
    
    def search(self, data):
        if self.__head == None:
            print('Please \'append\' data on the BlockChain before searching for it')
            return None
        else:
            placeholder = self.__head
            while placeholder is not None:
                if placeholder.data == data:
                    return placeholder
                placeholder = placeholder.previous_hash
            return None
    
    def to_list(self):
        output_list = []
        placeholder = self.__head
        while placeholder is not None:
            output_list.append([placeholder.data, placeholder.data, placeholder.hash])
            placeholder = placeholder.previous_hash


if __name__ == '__main__':
    blockchain = BlockChain()

    print(blockchain.size())
    # 0
    print(blockchain.to_list())
    # []

    blockchain.append('my balance: 0 | cash flow: +10 | final balance: 10')
    print(blockchain.size())
    # 1
    print(blockchain.to_list())
    # [['my balance: 0 | cash flow: +10 | final balance: 10', 1564306421.0008988, '5e5a93abe59f9e92b38e00ebc7a50c50f902f5a8
    # 210d327590a36ffb25a831d9']]
    blockchain.append('my balance: 10 | cash flow: +25 | final balance: 35')
    blockchain.append('my balance: 35 | cash flow: -15 | final balance: 20')
    blockchain.append('my balance: 20 | cash flow: +125 | final balance: 145')
    blockchain.append('my balance: 145 | cash flow: +5 | final balance: 150')
    print(blockchain.size())
    # 5
    print(blockchain.to_list())
    # [['my balance: 145 | cash flow: +5 | final balance: 150', 1564306378.6235423, '43841086a72ab23dacc07ac04341357ed73
    # 51a07f8c8f0df92056cd439f49302'], ['my balance: 20 | cash flow: +125 | final balance: 145', 1564306378.6235056, '597f
    # 549af039dbb1c79d5e4ae5c347189cf7b8bafc12011f44b0cc06692ade9e'], ['my balance: 35 | cash flow: -15 | final balance: 20'
    # , 1564306378.623468, '6da8edd2d3d03bfa69810f7390ce55a64bab5102b79e37c973a4bed4be303e77'], ['my balance: 10 |
    # cash flow: +25 | final balance: 35', 1564306378.6234293, 'ed240a001a354b3ee5f36db5ccdbcac1235806a106907feaedd9db02c
    # 6ee7dfc'], ['my balance: 0 | cash flow: +10 | final balance: 10', 1564306378.6233213, '5e5a93abe59f9e92b38e00ebc7a50
    # c50f902f5a8210d327590a36ffb25a831d9']]
    # Testing the "search function"
    print(blockchain.search('my balance: 20 | cash flow: +125 | final balance: 145'))
    # Block is:
    # Data: my balance: 20 | cash flow: +125 | final balance: 145
    # Timestamp: 1564305924.884146
    # Hash: 597f549af039dbb1c79d5e4ae5c347189cf7b8bafc12011f44b0cc06692ade9e
    # Edge Cases:
    print(blockchain.search('my balance: 1000 | cash flow: +100 | final balance: 1100'))
    # None
    blockchain = BlockChain()
    print(blockchain.search('my balance: 20 | cash flow: +125 | final balance: 145'))
    # Please 'append' data on the BlockChain before searching for it