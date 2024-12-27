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

    def visualize(self, filename="graph.png"):
        # NetworkX grafiğini oluştur
        G = nx.Graph()
        
        # Düğümleri ve kenarları ekle
        for node, neighbors in self.adj_list.items():
            G.add_node(node)
            for neighbor in neighbors:
                G.add_edge(node, neighbor)

        # Düğümleri yerleştirmek için bir düzen kullan
        pos = nx.spring_layout(G)

        # Düğümleri çiz (renkler ve boyutlar dinamik olabilir)
        node_colors = [self.get_node_color(node) for node in G.nodes()]
        node_sizes = [self.get_node_size(node) for node in G.nodes()]

        nx.draw_networkx_nodes(G, pos, node_color=node_colors, node_size=node_sizes)

        # Kenarları çiz (kalınlıklar dinamik olabilir)
        edge_widths = [self.get_edge_weight(u, v) for u, v in G.edges()]
        nx.draw_networkx_edges(G, pos, width=edge_widths)

        # Düğüm etiketlerini çiz
        nx.draw_networkx_labels(G, pos)

        # Grafik ayarları ve kaydetme
        plt.title("Graph Visualization")
        plt.axis("off")
        plt.savefig(filename, format="PNG")
        plt.close()