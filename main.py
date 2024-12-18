import pandas as pd
from author_node import Author
from pyvis.network import Network
from graph import Graph
from collections import defaultdict
import webbrowser

# Veriyi yükle
data = pd.read_excel('DATASET.xlsx', nrows=1000)

# Pyvis ağı - Fizik ayarları optimize edildi
g = Network(height="1500px", width="2000px", bgcolor='#444444', font_color='white', notebook=False)
g.barnes_hut()

# Graph nesnesi
graph = Graph()
unique_authors = {}  # Yazarların benzersiz olması için sözlük
edges = set()  # Tekrarlı kenarları engellemek için set kullanımı

# Makale bilgilerini işle ve bağlantıları oluştur
for _, row in data.iterrows():
    if pd.notna(row['coauthors']):
        # Ana yazar ve coauthor'ları al
        author = row['author_name'].strip() if pd.notna(row['author_name']) else "Unknown Author"
        coauthors = row['coauthors'].strip('[]').replace("'", "").split(',')
        coauthors = list(set(name.strip() for name in coauthors))  # Benzersiz coauthor listesi
        
        # Ana yazar düğümünü ekle
        if author not in unique_authors:
            unique_authors[author] = Author("None", author)
            graph.add_node(author)

        # Coauthor düğümlerini ekle ve ana yazarla bağlantı kur
        for coauthor in coauthors:
            # Eğer coauthor ana yazarın kendisiyle aynıysa, atla
            if coauthor == author:
                continue  # Kendisiyle bağlantı oluşturmayı engelle
            
            if coauthor not in unique_authors:
                unique_authors[coauthor] = Author("None", coauthor)
                graph.add_node(coauthor)
            
            # Sadece ana yazar ile coauthor arasında bağlantı oluştur
            edge = tuple(sorted((author, coauthor)))
            if edge not in edges:
                edges.add(edge)
                graph.add_edge(author, coauthor)
        

# Pyvis ağına düğümleri ekle
for author in unique_authors:
    size = min(20 + 2*len(graph.adj_list[author]), 150)  # Bağlantı sayısına göre boyut
    color = '#00aaff' if len(graph.adj_list[author]) > 10 else '#7777ff'
    g.add_node(author, label=author, size=size, color=color)

# Pyvis ağına kenarları ekle
print(len(unique_authors))
print(len(edges))
for edge in edges:
    g.add_edge(edge[0], edge[1], width=1)

# HTML çıktısını oluştur ve tarayıcıda aç
output_file = "fixed_graph.html"
g.write_html(output_file)
webbrowser.open(output_file)
