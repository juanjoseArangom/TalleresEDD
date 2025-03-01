# from collections import deque

# class TrieNode:
#     def __init__(self):
#         self.children = {}
#         self.is_end_of_word = False

# class Trie:
#     def __init__(self):
#         self.root = TrieNode()
#         self.count = 0

#     def insert(self, word):
#         node = self.root
#         for char in word:
#             if char not in node.children:
#                 node.children[char] = TrieNode()
#             node = node.children[char]
#         if not node.is_end_of_word:
#             node.is_end_of_word = True
#             self.count += 1

#     def search(self, word):
#         node = self.root
#         for char in word:
#             if char not in node.children:
#                 return False
#             node = node.children[char]
#         return node.is_end_of_word

#     def startsWithPrefix(self, prefix):
#         node = self.root
#         for char in prefix:
#             if char not in node.children:
#                 return False
#             node = node.children[char]
#         return len(node.children) > 0

#     def delete(self, word):
#         q = deque()
#         node = self.root
#         for char in word:
#             if char not in node.children:
#                 return False
#             else:
#                 q.append(node)
#                 node = node.children[char]
#         if len(node.children) > 0:
#             node.is_end_of_word = False
#         else:
#             for char in word[::-1]:
#                 node = q.pop()
#                 node.children.pop(char)
#                 if node.is_end_of_word or len(node.children) > 0:
#                     break
#             self.count -= 1
#             return True

#     def _traverseRecursively(self, node, current_word, words_list):
#         if node.is_end_of_word:
#             words_list.append(current_word)
#         for char, child_node in node.children.items():
#             self._traverseRecursively(child_node, current_word + char, words_list)

#     def traverse(self):
#         words_list = []
#         self._traverseRecursively(self.root, '', words_list)
#         return words_list

# while True:
#     e = int(input())
#     if e == 0:
#         break
#     trii = Trie()
#     for _ in range(e):
#         valido = True
#         adn = input()
#         for a in adn:
#             trii.insert(a)
#             if trii.startsWithPrefix(a):
#                 valido = False
#                 break
#     if valido:
#         print("TRUE")
#     else:
#         print("FALSE")

from collections import deque

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def startsWithPrefix(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True

def main():
    while True:
        e = int(input())
        if e == 0:
            break
        trii = Trie()
        valido = True
        adn_list = [input().strip() for _ in range(e)]

        for adn in adn_list:
            trii.insert(adn)

        for adn in adn_list:
            node = trii.root
            for i, char in enumerate(adn):
                if char not in node.children:
                    break
                node = node.children[char]
                if node.is_end_of_word and i < len(adn) - 1:
                    valido = False
                    break
            if not valido:
                break

        if valido:
            print("TRUE")
        else:
            print("FALSE")

if __name__ == "__main__":
    main()