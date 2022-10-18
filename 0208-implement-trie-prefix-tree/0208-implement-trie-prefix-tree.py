class TrieNode :
    def __init__(self, char = "") :
        self.char = char 
        self.children = {}
        self.is_end = False 
        
        
class Trie(object):

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        node = self.root 
        
        for char in word :
            if char in node.children :
                node = node.children[char]
            else :
                new_node = TrieNode(char)
                node.children[char] = new_node
                node = new_node 
        node.is_end = True 
        

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        node = self.root 
        for char in word :
            if char not in node.children :
                return False
            node = node.children[char]
        
        return node.is_end 

    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """
        node = self.root 
        for char in prefix :
            if char not in node.children :
                return False
            node = node.children[char]
        return True 


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)