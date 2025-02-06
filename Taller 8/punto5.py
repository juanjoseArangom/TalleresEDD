class Node(object):
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1
 
class AVLTree(object):
    def __init__(self):
        self.size = 0
        self.root = None
 
    def insert(self, key):
        if not self.search(key):
            self.root = self._insertRecursively(self.root, key)
 
    def _insertRecursively(self, root, key):
        if not root:
            self.size += 1
            return Node(key)
        elif key < root.key:
            root.left = self._insertRecursively(root.left, key)
        else:
            root.right = self._insertRecursively(root.right, key)
 
        root.height = 1 + max(self._getNodeHeight(root.left),
                              self._getNodeHeight(root.right))
 
        balanceFactor = self._getNodeBalance(root)
        if balanceFactor > 1:
            if key < root.left.key:
                return self._rightRotate(root)
            else:
                root.left = self._leftRotate(root.left)
                return self._rightRotate(root)
 
        if balanceFactor < -1:
            if key > root.right.key:
                return self._leftRotate(root)
            else:
                root.right = self._rightRotate(root.right)
                return self._leftRotate(root)
 
        return root
 
    def delete(self, key):
        if self.search(key):
            self.size -= 1
            self.root = self._deleteRecursively(self.root, key)
 
    def _deleteRecursively(self, root, key):
        if not root:
            return root
        elif key < root.key:
            root.left = self._deleteRecursively(root.left, key)
        elif key > root.key:
            root.right = self._deleteRecursively(root.right, key)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            temp = self._getMin(root.right)
            root.key = temp.key
            root.right = self._deleteRecursively(root.right, temp.key)
 
        root.height = 1 + max(self._getNodeHeight(root.left), self._getNodeHeight(root.right))
        balanceFactor = self._getNodeBalance(root)
 
        if balanceFactor > 1:
            if self._getNodeBalance(root.left) >= 0:
                return self._rightRotate(root)
            else:
                root.left = self._leftRotate(root.left)
                return self._rightRotate(root)
        if balanceFactor < -1:
            if self._getNodeBalance(root.right) <= 0:
                return self._leftRotate(root)
            else:
                root.right = self._rightRotate(root.right)
                return self._leftRotate(root)
        return root
 
    def _leftRotate(self, z):
        y = z.right
        aux = y.left
        y.left = z
        z.right = aux
        z.height = 1 + max(self._getNodeHeight(z.left), self._getNodeHeight(z.right))
        y.height = 1 + max(self._getNodeHeight(y.left), self._getNodeHeight(y.right))
        return y
 
    def _rightRotate(self, z):
        y = z.left
        aux = y.right
        y.right = z
        z.left = aux
        z.height = 1 + max(self._getNodeHeight(z.left), self._getNodeHeight(z.right))
        y.height = 1 + max(self._getNodeHeight(y.left), self._getNodeHeight(y.right))
        return y
 
    def _getNodeHeight(self, root):
        return 0 if not root else root.height
 
    def _getNodeBalance(self, root):
        return 0 if not root else self._getNodeHeight(root.left) - self._getNodeHeight(root.right)
 
    def _getMin(self, root):
        while root.left:
            root = root.left
        return root
 
    def _getMax(self, root):
        while root.right:
            root = root.right
        return root
 
    def search(self, key):
        return self._searchRecursively(self.root, key) is not None
 
    def _searchRecursively(self, root, key):
        if not root or root.key == key:
            return root
        if key < root.key:
            return self._searchRecursively(root.left, key)
        else:
            return self._searchRecursively(root.right, key)
 
    def popMin(self):
        if self.size == 0:
            return None
        key = self._getMin(self.root).key
        self.delete(key)
        return key
 
    def popMax(self):
        if self.size == 0:
            return None
        key = self._getMax(self.root).key
        self.delete(key)
        return key
 
def masa(m):
    arbol = AVLTree()
    for masa in m:
        arbol.insert(masa)
    while arbol.size > 1:
        minimo = arbol.popMin()
        maximo = arbol.popMax()
        diferencia = maximo - minimo
        if diferencia > 0:
            arbol.insert(diferencia)
    return arbol.root.key if arbol.root else 0
 
c = int(input())
for _ in range(c):
    entrada = list(map(int, input().split()))[:-1]  
    print(masa(entrada))