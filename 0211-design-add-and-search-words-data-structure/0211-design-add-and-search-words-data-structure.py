class Node:
    def __init__(self):
        self.child = {}
        self.fin = False

class WordDictionary:

    def __init__(self):
        self.root = Node()
        

    def addWord(self, word: str) -> None:
        cur = self.root
        for w in word:
            if w not in cur.child: cur.child[w] = Node()
            cur = cur.child[w]
        cur.fin = True
                
    def search(self, word: str) -> bool:
        def dfs(cur : Node, index : int) -> bool:
            if index == len(word):  return cur.fin
            
            if word[index] != '.':  return False if word[index] not in cur.child else dfs(cur.child[word[index]], index + 1)
                
            for childs in cur.child.values():
                if dfs(childs, index + 1):  return True
            return False
        return dfs(self.root, 0)
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)