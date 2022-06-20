from typing import List


class Node:
    def __init__(self):
        self.child = [None] * 26

# 길이별로 정렬하기

class Trie:
    def __init__(self):
        self.root = Node()

    def insertString(self, string: str):
        node = self.root
        flg = False
        
        for s in string:
            childIndex = ord(s) - ord('a')

            if not node.child[childIndex]:
                node.child[childIndex] = Node()
                flg = True #-> 한번이라도 새로운 노드를 만들면 다른 단어의 pre or suffix가 아님

            node = node.child[childIndex]
        
        return flg


class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        words.sort(key=lambda x: len(x), reverse=True)
        rvTrie = Trie()
        return sum(len(s) + 1 if rvTrie.insertString(s[::-1]) else 0 for s in words)
