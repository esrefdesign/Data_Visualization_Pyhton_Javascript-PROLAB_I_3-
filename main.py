import pandas as pd
from author_node import Author
from essay_node import Essay
from bstNode import BST,BSTNode
from priorityQueue import PriorityQueue
from graph import Graph
from collections import defaultdict
#import All neededs

data = pd.read_excel('DATASET.xlsx')

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


