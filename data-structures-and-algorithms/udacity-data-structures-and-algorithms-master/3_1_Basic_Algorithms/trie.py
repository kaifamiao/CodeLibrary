from collections import defaultdict


class TrieNode(object):
    def __init__(self):
        self.is_word = False
        self.children = defaultdict(TrieNode)


class Trie(object):
    def __init__(self):
        self.root = TrieNode()
    
    def add(self, word):
        node = self.root
        for i, char in enumerate(word):
            if i == len(word) - 1:
                node.children[char].is_word = True
            else:
                node = node.children[char]
    
    def exists(self, word):
        node = self.root
        for i, char in enumerate(word):
            if i == len(word) - 1:
                return node.children[char].is_word
            else:
                if char not in node.children:
                    return False
                node = node.children[char]


if __name__ == '__main__':
    word_list = ['apple', 'bear', 'goo', 'good', 'goodbye', 'goods', 'goodwill', 'gooses'  ,'zebra']
    word_trie = Trie()
    # Add words
    for word in word_list:
        word_trie.add(word)
    # Test words
    test_words = ['bear', 'goo', 'good', 'goos']
    for word in test_words:
        if word_trie.exists(word):
            print('"{}" is a word.'.format(word))
        else:
            print('"{}" is not a word.'.format(word))
    
    valid_words = ['the', 'a', 'there', 'answer', 'any', 'by', 'bye', 'their']
    word_trie = Trie()
    for valid_word in valid_words:
        word_trie.add(valid_word)

    # Tests
    assert word_trie.exists('the')
    assert word_trie.exists('any')
    assert not word_trie.exists('these')
    assert not word_trie.exists('zzz')
    print('All tests passed!')