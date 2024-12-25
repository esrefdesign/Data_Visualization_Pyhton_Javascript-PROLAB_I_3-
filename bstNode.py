

class Node:
    def __init__(self, author, left=None, right=None):
        self.author = author
        self.left = left
        self.right = right

class BST:
    def __init__(self):
        self.root = None

    def insert(self, author):
        if self.root is None:
            self.root = Node(author)
        else:
            self._insert(self.root, author)

    def _insert(self, node, author):
        if author < node.author:
            if node.left is None:
                node.left = Node(author)
            else:
                self._insert(node.left, author)
        else:
            if node.right is None:
                node.right = Node(author)
            else:
                self._insert(node.right, author)

    def inorder(self):
        return self._inorder(self.root)

    def _inorder(self, node):
        return self._inorder(node.left) + [node.author] + self._inorder(node.right) if node else []

    def get_edges(self):
        """Return edges of the BST as a list of tuples."""
        edges = []
        self._get_edges(self.root, edges)
        return edges

    def _get_edges(self, node, edges):
        if node:
            if node.left:
                edges.append((node.author, node.left.author))
                self._get_edges(node.left, edges)
            if node.right:
                edges.append((node.author, node.right.author))
                self._get_edges(node.right, edges)
