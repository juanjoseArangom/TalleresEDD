class TrieNode:
    def __init__(self):
        self.children = {}
        self.count = 0 

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
            node.count += 1  
        self.word_count[word] = self.word_count.get(word, 0) + 1

    def delete(self, word):
        if word not in self.word_count:
            return  
        node = self.root
        stack = []  
        for char in word:
            stack.append((node, char)) 
            node = node.children[char]
            node.count -= 1  
        
        self.word_count[word] -= 1
        if self.word_count[word] == 0:
            del self.word_count[word]
        while stack:
            parent, char = stack.pop()
            child = parent.children[char]
            if child.count == 0:
                del parent.children[char]
            else:
                break

    def query(self, k, h):
        node = self.root
        for _ in range(h):
            if not node.children:
                return "NO"
            char = next(iter(node.children)) 
            node = node.children[char]
        return "SI" if node.count >= k else "NO"

def main():
    p = int(input())
    trii = Trie()
    for _ in range(p):
        parts = input().split()
        op = int(parts[0])
        
        if op == 1:
            trii.insert(parts[1])
        elif op == 2:
            trii.delete(parts[1])
        elif op == 3:
            k, h = map(int, parts[1:])
            print(trii.query(k, h))

if __name__ == "__main__":
    main()
