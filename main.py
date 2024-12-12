import pandas as pd
from author_node import Author
from essay_node import Essay
from bstNode import BST,BSTNode
from priorityQueue import PriorityQueue
from graph import Graph
#import All neededs


# Excel'den veriyi çekme

data = pd.read_excel('DATASET.xlsx',nrows=400)

head = None
current = None

authors = data['author_name']
essays = data[['doi','paper_title']].drop_duplicates()

author_to_id = {author: idx for idx, author in enumerate(set(authors))}

# Her yazarı bir kez yazdırma
unique_authors = [{'Author': author, 'Author_ID': author_to_id[author]} for author in author_to_id]
unique_essay = [{'Essay_ID': row['doi'], 'Essay_Title': row['paper_title']} for _, row in essays.iterrows()]

for entry in unique_essay:
    new_author= Essay(entry['Essay_ID'],entry['Essay_Title'])
    if head is None:
        head = new_author # Set the head of the linked list
        current = head
    else:
        current.next = new_author  # Link the new essay
        current = new_author # Move to the new essay
    print(f"{current.name}    {current.Id}")


# Sonuçları yazdırma
for entry in unique_authors:
    new_author= Author(entry['Author_ID'],entry['Author'])
    if head is None:
        head = new_author # Set the head of the linked list
        current = head
    else:
        current.next = new_author  # Link the new essay
        current = new_author # Move to the new essay
    print(f"{current.name}    {current.Id}")

