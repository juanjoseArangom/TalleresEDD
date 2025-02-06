from collections import deque
 
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
            new_node = Node(key)
            self.size += 1
            return new_node
        elif key < root.key:
            root.left = self._insertRecursively(root.left, key)
        else:
            root.right = self._insertRecursively(root.right, key)
 
        root.height = 1 + max(self._getNodeHeight(root.left), self._getNodeHeight(root.right))
 
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
 
    def search(self, key):
        return self._searchRecursively(self.root, key) is not None
 
    def _searchRecursively(self, root, key):
        if root is None or root.key == key:
            return root
        if key < root.key:
            return self._searchRecursively(root.left, key)
        return self._searchRecursively(root.right, key)
 
    def _getNodeHeight(self, root):
        return root.height if root else 0
 
    def _getNodeBalance(self, root):
        return self._getNodeHeight(root.left) - self._getNodeHeight(root.right) if root else 0
 
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
 
    def anilloConcentrico(self):
        if not self.root:
            return ""
        queue = deque([self.root])
        result = []
        while queue:
            node = queue.popleft()
            children = 0
            if node.left:
                queue.append(node.left)
                children = -1 if not node.right else 2
            if node.right:
                queue.append(node.right)
                if not node.left:
                    children = 1
            result.append(str(children))
        return ".".join(result)
 
 
def main():
    while True:
        try:
            n = int(input().strip())
            if n == 0:
                break
            values = list(map(int, input().split()))
            arbol = AVLTree()
            for valor in values:
                arbol.insert(valor)
            print(arbol.anilloConcentrico())
        except EOFError:
            break
 
if __name__ == "__main__":
    main()