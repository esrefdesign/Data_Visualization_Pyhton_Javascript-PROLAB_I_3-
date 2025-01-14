import pandas as pd
from author_node import Author
from essay_node import Essay
from graph import Graph
from isterler import Wanted
from collections import defaultdict
import random
# Veriyi yükle
data = pd.read_excel('DATASET.xlsx', nrows=1000)


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
                unique_authors[coauthor] = Author(f"{random.randint(0,10000)}", coauthor)
                graph.add_node(coauthor)
            
            # Sadece ana yazar ile coauthor arasında bağlantı oluştur
            edge = tuple(sorted((author, coauthor)))
        

            if edge not in edges:
                edges.add(edge)
                graph.add_edge(author, coauthor)
        



