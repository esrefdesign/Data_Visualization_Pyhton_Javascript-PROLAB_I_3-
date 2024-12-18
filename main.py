import pandas as pd
from author_node import Author
from essay_node import Essay
from pyvis.network import Network
from graph import Graph
from isterler import Graph as CustomGraph, BST, PriorityQueueWrapper
import webbrowser
from collections import defaultdict

# Veriyi yükle
data = pd.read_excel('DATASET.xlsx', nrows=1000)

# Pyvis ağı - Fizik ayarları optimize edildi
g = Network(height="1500px", width="2000px", bgcolor='#333333', font_color='white', notebook=False)
g.barnes_hut()

# Graph nesneleri
graph = Graph()
custom_graph = CustomGraph()
unique_authors = {}
orcid_to_author = {}
author_to_coauthors = {}
edges = set()

# Makale bilgilerini işle ve bağlantıları oluştur
for _, row in data.iterrows():
    if pd.notna(row['coauthors']):
        author = row['author_name'].strip() if pd.notna(row['author_name']) else "Unknown Author"
        orcid = row['orcid'] if pd.notna(row['orcid']) else "Unknown ORCID"
        coauthors = row['coauthors'].strip('[]').replace("'", "").split(',')
        coauthors = list(set(name.strip() for name in coauthors))
        
        essay_title = row['paper_title'] if pd.notna(row['paper_title']) else "Unknown Title"
        essay_ID = row['doi'] if pd.notna(row['doi']) else "Unknown ID"

        essay = Essay(essay_ID, essay_title, coauthors)

        # Ana yazar düğümünü ekle
        if author not in unique_authors:
            unique_authors[author] = Author(orcid, author)
            orcid_to_author[orcid] = author
            graph.add_node(author)
            custom_graph.add_node(author)
            unique_authors[author].essay.add(essay)

        for coauthor in coauthors:
            if coauthor == author:
                continue
            if coauthor not in unique_authors:
                unique_authors[coauthor] = Author("None", coauthor)
                graph.add_node(coauthor)
                custom_graph.add_node(coauthor)

            edge = tuple(sorted((author, coauthor)))
            if edge not in edges:
                edges.add(edge)
                graph.add_edge(author, coauthor)
                custom_graph.add_edge(author, coauthor)
        if author not in author_to_coauthors:
            author_to_coauthors[author] = set()
        author_to_coauthors[author].update(coauthors)

author_to_coauthors = {author: list(coauthors) for author, coauthors in author_to_coauthors.items()}

# Pyvis ağına düğümleri ekle
for author_name, author_obj in unique_authors.items():
    size = min(20 + 2 * len(custom_graph.adj_list[author_name]), 150)
    color = '#00aaff' if len(custom_graph.adj_list[author_name]) > 10 else '#7777ff'
    essays_info = "".join(f"ID: {essay.ID}, Title: {essay.title}" for essay in author_obj.essay)
    tooltip = f"""
    Author: {author_name}
    ORCID: {author_obj.orcid}
    Essays:
    {essays_info if essays_info else "No Essays"}
    """
    g.add_node(author_name, label=author_name, size=size, color=color, title=tooltip)

# Pyvis ağına kenarları ekle
for edge in edges:
    g.add_edge(edge[0], edge[1], width=1)

# Wanted sınıfını başlat

# Kullanıcı Menüsü
def menu():
    print("""
    1. A ile B yazarı arasındaki en kısa yolu bul
    2. A yazarının işbirliği yaptığı yazarlar için kuyruk oluştur
    3. Kuyruktaki yazarlardan bir BST oluştur
    4. A yazarının işbirliği yaptığı yazar sayısını hesapla
    5. En çok işbirliği yapan yazarı belirle
    6. Görsel grafiği tarayıcıda görüntüle
    7. Çıkış
    """)

while True:
    menu()
    choice = input("Bir seçenek giriniz: ")

    if choice == "1":
        a = input("Başlangıç yazarı: ")
        b = input("Hedef yazarı: ")
        distance, path = custom_graph.dijkstra(a, b)
        print(f"En kısa yol mesafesi: {distance}")
        print(f"Yol: {' -> '.join(path)}")

    elif choice == "2":
        a = input("Yazar adı: ")
        pq = PriorityQueueWrapper()
        for coauthor, weight in custom_graph.adj_list[a]:
            pq.add(coauthor, weight)
        print("Ağırlıklarına göre sıralanmış işbirlikçi yazarlar:")
        while not pq.is_empty():
            print(pq.pop())

    elif choice == "3":
        bst = BST()
        for author in custom_graph.adj_list.keys():
            bst.insert(author)
        print("BST içeriği (inorder):", bst.visualize())

    elif choice == "4":
        a = input("Yazar adı: ")
        count = len(custom_graph.adj_list[a])
        print(f"{a} yazarının işbirliği yaptığı toplam yazar sayısı: {count}")

    elif choice == "5":
        most_collab = max(custom_graph.adj_list, key=lambda author: len(custom_graph.adj_list[author]))
        print(f"En çok işbirliği yapan yazar: {most_collab}")

    elif choice == "6":
        output_file = "graph_visualization.html"
        g.write_html(output_file)
        print("Grafik tarayıcıda görüntüleniyor...")
        webbrowser.open(output_file)

    elif choice == "7":
        print("Programdan çıkılıyor...")
        break

    else:
        print("Geçersiz seçenek! Tekrar deneyin.")
