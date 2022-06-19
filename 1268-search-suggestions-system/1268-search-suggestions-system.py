from typing import List

class Node:
    def __init__(self):
        self.child = [None] * 26
        self.maxIndex = 0
        self.count = 0

class Trie:
    def __init__(self, strings : List[str]):
        self.stringList = strings
        self.root = Node()

        for i in range(len(self.stringList)):
            self.insert(self.stringList[i], i + 1)


    def insert(self, string : str, code : int):
        node : Node = self.root

        for s in string:
            childIdx : int = ord(s) - ord("a")

            if not node.child[childIdx]:
                node.child[childIdx] : Node = Node()

            node : Node = node.child[childIdx]

            if node.count < 3:
                node.maxIndex : int = code
                node.count += 1

    def search(self, string : str):
        resultByLength = [[] for _ in range(len(string))]
        node = self.root

        for i in range(len(string)):
            s : str = string[i]
            childIdx: int = ord(s) - ord("a")

            if not node.child[childIdx]: break

            node : Node = node.child[childIdx]
            resultByLength[i].extend(self.stringList[node.maxIndex - node.count: node.maxIndex])

        return resultByLength
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()

        trie = Trie(products)
        return trie.search(searchWord)

