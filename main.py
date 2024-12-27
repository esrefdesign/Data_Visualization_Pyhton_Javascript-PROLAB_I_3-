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
# g = Network(height="1500px", width="2000px", bgcolor='#444444', font_color='white', notebook=False)
# g.barnes_hut()

# Graph nesnesi
graph = Graph()
unique_authors = defaultdict()  # Yazarların benzersiz olması için sözlük
edges = set() 
unique_essasys= list() # Tekrarlı kenarları engellemek için set kullanımı

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
        
        # Ana yazar düğümünü ekle
        if author not in unique_authors:
            unique_authors[author] = Author(author_Id, author)
            graph.add_node(author)
        
        current_essay= Essay(essay_ID,essay_title,coauthors)
        unique_authors[author].essay.append(current_essay)
        
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
# for author,author_obj in unique_authors.items():
#     size = min(20 + 2*len(graph.adj_list[author]), 150)  # Bağlantı sayısına göre boyut
#     color = '#00aaff' if len(graph.adj_list[author]) > 5 else '#7777ff'
#     essays = [f"{essay.title} (ID: {essay.ID})" for essay in author_obj.essay]  # Makale bilgilerini al
#     essays_text = "\n".join(essays) if essays else "No essays available"

#     title = f"""
#     {author}
#     Connections:{len(graph.adj_list[author])}
#     Essays:{essays_text}
#     """ if len(graph.adj_list[author])!=1 else f"""
#     {author}
#     Connections:{graph.adj_list[author]}
#     Essays:{essays_text}
#     """
   
   
#     g.add_node(author, label=author,title=title, size=size, color=color)

# # Pyvis ağına kenarları ekle


# print(len(edges))

# for edge in edges:
#     weight = graph.get_edge_weight(edge[0], edge[1])
#     if(weight>1):
#         print(weight)  # Get the collaboration count (edge weight)
#     g.add_edge(edge[0], edge[1], width=weight, weight=weight)


