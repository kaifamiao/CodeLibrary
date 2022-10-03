from collections import defaultdict


class TrieNode(object):
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.is_word = False
        
    def get_suffixes(self):
        suffixes = list([])
        self._get_suffixes(self.children, '', suffixes)
        return suffixes
    
    def _get_suffixes(self, root, suffix, suffix_list):
        for char, node in root.items():
            if node.is_word:
                suffix_list.append(suffix + char + " ")
            self._get_suffixes(node.children, suffix + char, suffix_list)


class Trie(object):
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            node = node.children[char]
        node.is_word = True
            
    def find(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return node
    
    def suffixes(self, prefix):
        node = self.find(prefix)
        suffixes =  node.get_suffixes()
        return "".join(suffixes).strip(" ").split(" ")


if __name__ == '__main__':
    MyTrie = Trie()
    wordList = [
        "ant", "anthology", "antagonist", "antonym", 
        "fun", "function", "factory", 
        "trie", "trigger", "trigonometry", "tripod"
    ]
    for word in wordList:
        MyTrie.insert(word)

    print ("Pass" if ("hology, agonist, onym" == ", ".join(MyTrie.suffixes("ant"))) else "Fail")
    print ("Pass" if ("un, unction, actory" == ", ".join(MyTrie.suffixes("f"))) else "Fail")
    print ("Pass" if ("rie, rigger, rigonometry, ripod" == ", ".join(MyTrie.suffixes("t"))) else "Fail")
    print ("Pass" if ("ger, onometry" == ", ".join(MyTrie.suffixes("trig"))) else "Fail")