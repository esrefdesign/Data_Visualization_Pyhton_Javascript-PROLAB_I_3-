import pandas as pd
from author_node import Author
from essay_node import Essay
from pyvis.network import Network
from graph import Graph
from isterler import Wanted
from collections import defaultdict
import webbrowser

# Veriyi yükle
data = pd.read_excel('DATASET.xlsx', nrows=1000)
# Pyvis ağı - Fizik ayarları optimize edildi
g = Network(height="1500px", width="2000px", bgcolor='#444444', font_color='white', notebook=False)
g.barnes_hut()

# Graph nesnesi
graph = Graph()
unique_authors = defaultdict()  # Yazarların benzersiz olması için sözlük
edges = set() 
unique_essasys= defaultdict() # Tekrarlı kenarları engellemek için set kullanımı

# Makale bilgilerini işle ve bağlantıları oluştur
for _, row in data.iterrows():
    if pd.notna(row['coauthors']):
        # Ana yazar ve coauthor'ları al
        author = row['author_name'].strip() if pd.notna(row['author_name']) else "Unknown Author"
        author_Id=row['orcid'] if pd.notna(row['orcid']) else "Unknown ID"
        coauthors = row['coauthors'].strip('[]').replace("'", "").split(',')
        essay_title = row['paper_title']
        essay_ID = row['doi']
        coauthors = list(set(name.strip() for name in coauthors))  # Benzersiz coauthor listesi
        
        if essay_ID not in unique_essasys:
            unique_essasys[essay_ID]= Essay(essay_ID,essay_title,coauthors)
            
        # Ana yazar düğümünü ekle
        if author not in unique_authors:
            unique_authors[author] = Author(author_Id, author)
            unique_authors[author].essay.add(unique_essasys[essay_ID])
            graph.add_node(author)

        # Coauthor düğümlerini ekle ve ana yazarla bağlantı kur
        for coauthor in coauthors:
            # Eğer coauthor ana yazarın kendisiyle aynıysa, atla"
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
    color = '#00aaff' if len(graph.adj_list[author]) > 5 else '#7777ff'
    g.add_node(author, label=author, size=size, color=color)

wanteds = Wanted(unique_authors,unique_essasys)

# Pyvis ağına kenarları ekle

print(wanteds.wanted_5('R. Kumar'))

print(len(edges))

for edge in edges:
    g.add_edge(edge[0], edge[1], width=1)

# HTML çıktısını oluştur ve tarayıcıda aç
output_file = "fixed_graph.html"


g.set_options("""
var options = {
  "physics": {
    "enabled": true,
    "solver": "forceAtlas2Based",
    "forceAtlas2Based": {
      "gravitationalConstant": -50,
      "centralGravity": 0.01,
      "springLength": 50,
      "springConstant": 0.02
    },
    "maxVelocity": 50,
    "minVelocity": 0.1
  }
}
""")


g.write_html(output_file)


js_link = '<script src="custom_script.js"></script>'

# HTML dosyasını düzenle
with open(output_file, "r", encoding="utf-8") as file:
    html_content = file.read()

# </head>'den önce JavaScript dosyasını ekleyin
if js_link not in html_content:  # Aynı script eklenmesin diye kontrol
    html_content = html_content.replace("</head>", f"{js_link}\n</head>")

# Düzenlenmiş HTML'yi geri yaz
with open(output_file, "w", encoding="utf-8") as file:
    file.write(html_content)

# webbrowser.open(output_file)

