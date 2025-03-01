from collections import deque

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False
        self.count = 0

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            node.count += 1  
        node.is_end_of_word = True

    def shortest_unique_prefix(self, word):
        node = self.root
        prefix = ""
        for char in word:
            prefix += char
            node = node.children[char]
            if node.count == 1: 
                return prefix
        return prefix  

while True:
    a = int(input())
    if a == 0:
        break
    trii = Trie()
    asteroides = []
    for _ in range(a):
        name = input()
        asteroides.append(name)
        trii.insert(name)
    cantidad = sum(len(trii.shortest_unique_prefix(name)) for name in asteroides)
    print(cantidad)