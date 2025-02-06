class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1
 
class AVLTree:
    def __init__(self):
        self.root = None
 
    def insert(self, key):
        self.root = self._insert(self.root, key)
 
    def _insert(self, root, key):
        if not root:
            return Node(key)
        
        if key < root.key:
            root.left = self._insert(root.left, key)
        else:
            root.right = self._insert(root.right, key)
 
        root.height = 1 + max(self._getHeight(root.left), self._getHeight(root.right))
        balance = self._getBalance(root)
 
        if balance > 1 and key < root.left.key:
            return self._rightRotate(root)
 
        if balance < -1 and key > root.right.key:
            return self._leftRotate(root)
 
        if balance > 1 and key > root.left.key:
            root.left = self._leftRotate(root.left)
            return self._rightRotate(root)
 
        if balance < -1 and key < root.right.key:
            root.right = self._rightRotate(root.right)
            return self._leftRotate(root)
 
        return root
 
    def _leftRotate(self, z):
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        z.height = max(self._getHeight(z.left), self._getHeight(z.right)) + 1
        y.height = max(self._getHeight(y.left), self._getHeight(y.right)) + 1
        return y
 
    def _rightRotate(self, z):
        y = z.left
        T3 = y.right
        y.right = z
        z.left = T3
        z.height = max(self._getHeight(z.left), self._getHeight(z.right)) + 1
        y.height = max(self._getHeight(y.left), self._getHeight(y.right)) + 1
        return y
 
    def _getHeight(self, root):
        if not root:
            return 0
        return root.height
 
    def _getBalance(self, root):
        if not root:
            return 0
        return self._getHeight(root.left) - self._getHeight(root.right)
 
    def getHojasFinales(self):
        if not self.root:
            return 0
        max_depth = self._getMaxAltura(self.root)
        return self._getHojasMaxAltura(self.root, max_depth, 1)
 
    def _getMaxAltura(self, root):
        if not root:
            return 0
        left_depth = self._getMaxAltura(root.left)
        right_depth = self._getMaxAltura(root.right)
        return max(left_depth, right_depth) + 1
 
    def _getHojasMaxAltura(self, root, max_depth, current_depth):
        if not root:
            return 0
        if not root.left and not root.right:
            if current_depth == max_depth:
                return 1
            return 0
        return self._getHojasMaxAltura(root.left, max_depth, current_depth + 1) + \
               self._getHojasMaxAltura(root.right, max_depth, current_depth + 1)
 
 
 
c = int(input())
for _ in range(c):
    arbol = AVLTree()
    entrada = list(map(int, input().split()))
    for value in entrada:
        if value == -1:
            break
        arbol.insert(value)
    print(arbol.getHojasFinales())