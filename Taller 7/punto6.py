<<<<<<< HEAD
N = 6
valores = [13, 27, 9, 45, 36, 18]
eliminados = []

while len(valores) > 0:
    max_residuo = -1
    indice_a_eliminar = -1
    for i in range(len(valores)):
        residuo = valores[i] % len(valores)
        if residuo > max_residuo:
            max_residuo = residuo
            indice_a_eliminar = i
    eliminados.append(valores.pop(indice_a_eliminar))

for elemento in eliminados:
    print(elemento)
=======
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insertRecursively(self.root, key)

    def _insertRecursively(self, root, key):
        if root is None:
            return Node(key)
        if key < root.key:
            root.left = self._insertRecursively(root.left, key)
        elif key > root.key:
            root.right = self._insertRecursively(root.right, key)
        return root

    def search(self, key):
        if self._searchRecursively(self.root, key) != None:
            return True
        else:
            return False

    def _searchRecursively(self, root, key):
        if root is None or root.key == key:
            return root
        if key < root.key:
            return self._searchRecursively(root.left, key)
        return self._searchRecursively(root.right, key)

    def delete(self, key):
        self.root = self._deleteRecursively(self.root, key)

    def _deleteRecursively(self, root, key):
        if root is None:
            return root
        if key < root.key:
            root.left = self._deleteRecursively(root.left, key)
        elif key > root.key:
            root.right = self._deleteRecursively(root.right, key)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            root.key = self._minValueNode(root.right).key
            root.right = self._deleteRecursively(root.right, root.key)
        return root

    def _minValueNode(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def preOrder(self):
        elements = []
        self._preOrderRecursively(self.root, elements)
        return elements
    
    def _preOrderRecursively(self, root, elements):
        if root:
            elements.append(root.key)
            self._preOrderRecursively(root.left, elements)
            self._preOrderRecursively(root.right, elements)

    def inOrder(self):
        elements = []
        self._inOrderRecursively(self.root, elements)
        return elements

    def _inOrderRecursively(self, root, elements):
        if root.left != None and root.right != None:
            self._inOrderRecursively(root.left, elements)
            self._inOrderRecursively(root.right, elements)
        else:
            elements.append(root.key)

    def altura(self, nodo=None):
        if nodo is None:
            nodo = self.root
        if nodo is None:
            return 0
        stack = [(nodo, 1)] 
        max_altura = 0
        while stack:
            actual, nivel = stack.pop()
            if actual:
                max_altura = max(max_altura, nivel)  
                stack.append((actual.left, nivel + 1))  
                stack.append((actual.right, nivel + 1))  
        return max_altura
    
    def contar_hojas(self, nodo=None):
        if nodo is None:
            nodo = self.root
        if nodo is None: 
            return 0
        if nodo.left is None and nodo.right is None: 
            return 1
        return self.contar_hojas(nodo.left) + self.contar_hojas(nodo.right)
    
    def hijos_unicos(self):
        if self.root is None:
            return 0
        contador = 0
        stack = [self.root] 
        while stack:
            nodo = stack.pop()
            if (nodo.left is None and nodo.right is not None) or (nodo.left is not None and nodo.right is None):
                contador += 1
            if nodo.left:
                stack.append(nodo.left)
            if nodo.right:
                stack.append(nodo.right)

        return contador
    
    def imprimir_arbol(self, nodo=None, nivel=0, resultado=None):
        if resultado is None:
            resultado = []
        if nodo is None:
            nodo = self.root
        if nodo.right:
            self.imprimir_arbol(nodo.right, nivel + 1, resultado)
        resultado.append('\t' * nivel + str(nodo.key))
        if nodo.left:
            self.imprimir_arbol(nodo.left, nivel + 1, resultado)

        return resultado

    def es_completo(self):
        if self.root is None:
            return True  

        queue = [self.root]
        encontrado_nulo = False

        while queue:
            nodo = queue.pop(0)
            if nodo:
                if encontrado_nulo:
                    return 
                queue.append(nodo.left)
                queue.append(nodo.right)
            else:
                encontrado_nulo = True 

        return True
    
c = int(input())
resultados = []

for _ in range(c):
    arbol = BinarySearchTree()
    entrada = list(map(int, input().split()))
    for valor in entrada:
        if valor == -1:  
            break
        arbol.insert(valor)
    if arbol.es_completo():
        resultados.append("completo")
    else:
        resultados.append("no")
print('\n'.join(resultados))
>>>>>>> 0dc63b232076fb9e531efdbc36dd862f7fe826ae
