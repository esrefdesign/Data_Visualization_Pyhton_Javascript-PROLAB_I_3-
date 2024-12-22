from collections import defaultdict

class Graph:
    def __init__(self):
        self.adj_list = defaultdict(list)  # Bağlantı listesi
        self.node_degrees = defaultdict(int)  # Düğümlerin bağlantı sayıları
        self.edge_counts = defaultdict(int)
        
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

    