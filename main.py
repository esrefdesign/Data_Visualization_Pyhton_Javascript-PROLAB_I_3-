import pandas as pd
from author_node import Author
from essay_node import Essay
from pyvis.network import Network
from bstNode import BST,BSTNode
from priorityQueue import PriorityQueue
from graph import Graph
from collections import defaultdict
#import All neededs

data = pd.read_excel('DATASET.xlsx')

g = Network(height="1500px",width="2000", bgcolor= '#222222', font_color='white')
g.add_nodes([1,2,3], value=[10, 100, 400],
    title=['I am node 1', 'node 2 here', 'and im node 3'],
    x=[21.4, 54.2, 11.2],
    y=[100.2, 23.54, 32.1],
    label=['NODE 1', 'NODE 2', 'NODE 3'],
    color=['#00ff1e', '#162347', '#dd4b39'])

# HTML dosyasını oluştur
g.write_html("graph.html")


# Manuel olarak tarayıcıda aç
import webbrowser
webbrowser.open("test.html")

authors = data[['author_name','orcid']].drop_duplicates()
essays = data[['doi','paper_title','coauthors']].drop_duplicates()

essay_nodes =  defaultdict(str)
unique_authors = defaultdict(str)

for _, row in authors.iterrows():
    author = Author(row['orcid'],row['author_name'])
    unique_authors[row['orcid']] = author

for orcid, paper_title ,doi,coauthors in zip(authors['orcid'],essays['paper_title'],essays['doi'],essays['coauthors']):
    coauthors_array = coauthors.strip('[]').replace("'", "").split(',')
    coauthors_array = [name.strip() for name in coauthors_array]
    
    essay = Essay(doi,paper_title,coauthors_array)
    unique_authors[orcid].essay.add(essay)

for orcid in unique_authors.values():
    for a in orcid.essay:
        for b in a.coauthors:
            print(b)


