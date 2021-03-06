from TrieNode import TrieNode
class Trie:
    
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word):
        node = self.root
        node.prefixCount += 1
        word = list(word)
        for c in word:
            node = node.getOrCreateChild(c)
            node.prefixCount += 1
        node.isFinal = True
    
    def query(self, word):
        node = self.root
        words = list(word)
        for c in words:
            if c in node.childrens:
                node = node.childrens[c]
            else:
                node = None               
            if node == None:
                return False
        return node.isFinal
    
    def remove(self, word):
        node = self.root
        words = list(word)
        for c in words:
            if c in node.childrens:
                node = node.childrens[c]
            else:
                node = None               
            if node == None:
                return
        node.isFinal = False
        
    def getNodeSequence(self, word):
        node = self.root
        nodes = []
        
        words = list(word)
        for c in words:
            if c in node.childrens:
                node = node.childrens[c]
                tup = (c, node)
                nodes.append(tup)
            else:
                node = None
            if node == None:
                return nodes
        return nodes
    
    def remove_from_Trie(self, word):
        nodes = self.getNodeSequence(word)
        for i in range(0, len(nodes)):             
             nodes[i][1].prefixCount -= 1
             if nodes[i][1].prefixCount == 0:
                 if i != 0:
                     nodes[i-1][1].childrens.pop(nodes[i][0])
                     print("Removed = ", nodes[i][0])
        self.root.prefixCount -= 1
        nodes[len(nodes) - 1][1].isFinal = False
        
    def wordsWithSamePrefix(self, prefix):
        node = self.root
        prefix = list(prefix)
        for c in prefix:
            if c in node.childrens:
                node = node.childrens[c]
            else:
                node = None
            if node == None:
                return 0
        return node.prefixCount
    
    def removeWordsPrefix(self, prefix):
        nodes = self.getNodeSequence(prefix)
        for i in range(0, len(nodes)):
            count = nodes[i][1].prefixCount
        nodes[i-1][1].childrens.pop(nodes[i][0])
        nodes[i-1][1].prefixCount -= count
        self.root.prefixCount -= count
        nodes[len(nodes) - 1][1].isFinal = False     

    def shortestUniquePrefix(self, node):
        ''' Print the shorest unique prefix 
        of all the given words '''
    def traverse(self, node, path):
        for key in node.childrens:
            print(key)
            child = node.childrens[key]
            self.printChild(child, path)
            
    def printChild(self, child, path):
        for key in child.childrens:
            print(key)
            descend = child.childrens[key]
            self.traverse(descend, path)

path = []
myTrie = Trie()
myTrie.insert('round')
myTrie.insert('roll')
myTrie.insert('tea')
myTrie.insert('to')
myTrie.insert('tour')
print(myTrie.query('round'))
print("No of unique words = ", myTrie.root.uniqueWords())
print("No of words with prefix = ", myTrie.wordsWithSamePrefix('to'))
myTrie.traverse(myTrie.root, path)
