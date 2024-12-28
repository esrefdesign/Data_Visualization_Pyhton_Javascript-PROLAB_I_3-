import networkx as nx
import matplotlib.pyplot as plt
class Node:
    def __init__(self, author, left=None, right=None):
        self.author = author
        self.left = left
        self.right = right

class BST:
    def __init__(self):
        self.root = None
        self.graph= None
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

    def build_from_graph(self, graph, start_author):
        """
        Grafikten yazarları alıp dengeli bir BST oluşturur.
        """
        visited = set()
        queue = [start_author]
        
        while queue:
            author = queue.pop(0)
            if author not in visited:
                self.insert(author)
                visited.add(author)
                queue.extend(graph.adj_list.get(author, []))

    def visualize(self, filename="web/static/bst_visualization.png"):
        """
        BST'yi bir grafik olarak görselleştirir ve kaydeder.
        """
        if not self.root:
            raise ValueError("Ağaç boş, görselleştirilecek düğüm yok.")

        # NetworkX grafiğini oluştur
        G = nx.DiGraph()
        edges = self.get_edges()
        G.add_edges_from(edges)

        # Düğümleri yerleştirmek için düzen
        pos = nx.spring_layout(G) # 'dot' düzenini kullan

        # Düğümleri ve kenarları çiz
        plt.figure(figsize=(10, 10))
        nx.draw(G, pos, with_labels=True, arrows=False, node_size=2000, node_color="lightblue", font_size=10)
        
        # Başlık ve kaydetme
        plt.title("Balanced BST Visualization")
        plt.savefig(filename, format="PNG", bbox_inches="tight")
        plt.close()
        return filename