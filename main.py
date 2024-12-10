import pandas as pd
from author_node import Author
from essay_node import Essay
from bstNode import BST,BSTNode
from priorityQueue import PriorityQueue
from graph import Graph
from collections import Counter
#import All neededs


# Excel'den veriyi çekme

data = pd.read_excel('DATASET.xlsx')




head = None
current = None
authors = data['author_name']

author_to_id = {author: idx for idx, author in enumerate(set(authors))}

# Her yazarı bir kez yazdırma
unique_authors = [{'Author': author, 'Author_ID': author_to_id[author]} for author in author_to_id]

# Sonuçları yazdırma
for entry in unique_authors:
    new_author= Author(entry['Author'],entry['Author_ID'])
    if head is None:
        head = new_author # Set the head of the linked list
        current = head
    else:
        current.next = new_author  # Link the new essay
        current = new_author # Move to the new essay
    print(f"{current.name}    {current.Id}")

    


# Create the linked list
# for index, row in data.iterrows():
#     essay_id = row['doi']
#     essay_title = row['paper_title']
#     essay_authors = row['coauthors']
#     essay_author = row['author_name']
    
#     new_essay = Author(essay_id, essay_title,essay_authors)

#     if head is None:
#         head = new_essay  # Set the head of the linked list
#         current = head
#     else:
#         current.next = new_essay  # Link the new essay
#         current = new_essay  # Move to the new essay

# while head:
#     print(head.getAuthors())
#     head = head.next
