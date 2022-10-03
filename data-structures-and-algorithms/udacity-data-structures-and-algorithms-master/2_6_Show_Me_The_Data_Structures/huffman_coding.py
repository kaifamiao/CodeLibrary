import sys
from collections import Counter
from heapq import heapify, heappush,heappop  


class CharFrequency(object):
    """
    CharFrequency holds characters and their frequencies. It only implements __lt__
    magic method in order to feed it into a minimum priority queue.
    """
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq

    def __lt__(self, other):
        return self.freq < other.freq
    
    def __str__(self):
        return '{}: {}'.format(self.char, int(self.freq))


class Tree(object):
    def __init__(self):
        self.__root = None
    
    


def huffman_encoding(data):
    char_frequencies = Counter(list(data))
    char_frequencies = [CharFrequency(char, freq) for char, freq in char_frequencies.items()]
    heapify(char_frequencies)

    while len(char_frequencies) != 0:
        print(heappop(char_frequencies))


def huffman_decoding(data,tree):
    pass


if __name__ == "__main__":
    huffman_encoding('abcd ddac')
    # codes = {}
    # a_great_sentence = "The bird is the word"
    # print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    # print ("The content of the data is: {}\n".format(a_great_sentence))
    # encoded_data, tree = huffman_encoding(a_great_sentence)
    # print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    # print ("The content of the encoded data is: {}\n".format(encoded_data))
    # decoded_data = huffman_decoding(encoded_data, tree)
    # print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    # print ("The content of the encoded data is: {}\n".format(decoded_data))