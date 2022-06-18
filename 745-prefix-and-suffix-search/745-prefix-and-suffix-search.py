from typing import List


class Node:
    def __init__(self):
        self.child = [None] * 27  # 26 alphabet / 1 {
        self.value = -1


class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word: str, index: int) -> None:
        node = self.root

        for spell in word:
            child = ord(spell) - ord("a")

            if not node.child[child]:
                node.child[child] = Node()

            node = node.child[child]
            node.value = index

    def search(self, word: str) -> int:
        node = self.root
        for spell in word:
            child = ord(spell) - ord("a")

            if not node.child[child]:
                return -1

            node = node.child[child]
        return node.value


class WordFilter:

    def __init__(self, words: List[str]):
        self.FilterTree = Trie()

        for index, word in enumerate(words):
            for i in range(1, min(11, len(word) + 1)):
                # 1 ~ 11개까지
                self.FilterTree.insert(word=word[-i:] + "{" + word, index=index)

    def f(self, prefix: str, suffix: str) -> int:
        return self.FilterTree.search(suffix + "{" + prefix)

    # Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(prefix,suffix)