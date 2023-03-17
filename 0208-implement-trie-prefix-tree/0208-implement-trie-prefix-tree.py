class Node:
    def __init__(self, end = False):
        self.end = end
        self.child = dict()

class Trie:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        cur = self.root
        for w in word:
            if w not in cur.child: cur.child[w] = Node()
            cur = cur.child[w]       
        cur.end = True

    def search(self, word: str) -> bool:
        cur = self.root
        for w in word:
            if w not in cur.child: return False
            cur = cur.child[w]
        return cur.end

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for w in prefix:
            if w not in cur.child: return False
            cur = cur.child[w]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)