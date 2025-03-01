import sys
import string

class TrieNode:
    def __init__(self):
        self.children = {}
        self.words = set()

class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.word_count = {}

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            node.words.add(word)
        self.word_count[word] = self.word_count.get(word, 0) + 1

    def search_prefix(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return []
            node = node.children[char]
        
        words = list(node.words)
        words.sort(key=lambda w: (-self.word_count[w], w))  
        return words

def clean_text(text):
    translator = str.maketrans(string.punctuation, ' ' * len(string.punctuation))
    return text.translate(translator).lower().split()

def main():
    L = int(input().strip())
    trii = Trie()
    for _ in range(L):
        words = clean_text(input().strip())
        for word in words:
            trii.insert(word)
    C = int(input().strip())
    for _ in range(C):
        prefix = input().strip().lower()
        result = trii.search_prefix(prefix)
        print(" ".join(result) if result else "-")

if __name__ == "__main__":
    main()
