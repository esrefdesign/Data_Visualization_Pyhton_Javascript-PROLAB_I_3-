from collections import defaultdict
import networkx as nx
import matplotlib.pyplot as plt

class Graph:
    def __init__(self):
        self.adj_list = defaultdict(list)  # Bağlantı listesi
        self.node_degrees = defaultdict(int)  # Düğümlerin bağlantı sayıları
        self.edge_counts = defaultdict(int)
        self.edge_weights = defaultdict(lambda: defaultdict(int))

    def add_node(self, author):
        if author not in self.adj_list:
            self.adj_list[author] = []  # Boş bir liste ile düğümü ekle
            self.node_degrees[author] = 0
            

    def add_edge(self, author1, author2):
        if author2 not in self.adj_list[author1]:
            self.adj_list[author1].append(author2)
            self.adj_list[author2].append(author1)
            self.node_degrees[author1] += 1
            self.node_degrees[author2] += 1

        self.edge_weights[author1][author2] += 1
        self.edge_weights[author2][author1] += 1  # Karşılıklı işbirliği

    def get_max_connected_node(self):
        return max(self.node_degrees, key=self.node_degrees.get, default=None)

    def get_node_size(self, author):
        """Bağlantı sayısına göre düğüm boyutunu hesapla."""
        return 20 + self.node_degrees[author] * 2  # Temel boyut + bağlantı sayısına göre büyüme

    def get_node_color(self, author):
        """Bağlantı sayısına göre düğüm rengini beyazdan sarıya doğru değiştir."""
        degree = self.node_degrees[author]
        yellow_intensity = min(255, degree * 20)  # Sarı tonları arttıkça yoğunlaşır
        return f"rgb({yellow_intensity}, {yellow_intensity}, 255)"
    
    def get_edge_thickness(self, author1, author2):
        """Bağlantı sayısına göre kenar kalınlığını hesapla."""
        return 1 + self.edge_counts[(author1, author2)] * 3  # Temel kalınlık + bağlantı sayısına göre artış

    
    def get_edge_weight(self, author1, author2):
        """İki yazar arasındaki işbirliği sayısını döndür."""
        return self.edge_weights[author1].get(author2, 0)
    
    def visualize(self,bst, filename="graph.png"):
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