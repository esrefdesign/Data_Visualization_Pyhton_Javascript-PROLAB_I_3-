
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

    def remove(self, author):
        self.root = self._remove(self.root, author)

    def _remove(self, node, author):
        if node is None:
            return node
        if author < node.author:
            node.left = self._remove(node.left, author)
        elif author > node.author:
            node.right = self._remove(node.right, author)
        else:
            # Node with one child or no child
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left

            # Node with two children: Get the inorder successor (smallest in the right subtree)
            min_node = self._min_value_node(node.right)
            node.author = min_node.author
            node.right = self._remove(node.right, min_node.author)
        return node

    def _min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def inorder(self):
        return self._inorder(self.root)

    def _inorder(self, node):
        return self._inorder(node.left) + [node.author] + self._inorder(node.right) if node else []

    def visualize(self):
        return self.inorder()
