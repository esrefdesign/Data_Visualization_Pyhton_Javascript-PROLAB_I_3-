import pandas as pd
from author_node import Author;
from essay_node import Essay;

# Excel'den veriyi çekme
data = pd.read_excel('DATASET.xlsx',nrows=20)

essay_data = data[['doi', 'paper_title','coauthors','author_name']]


head = None
current = None
# Create the linked list
for index, row in essay_data.iterrows():
    essay_id = row['doi']
    essay_title = row['paper_title']
    essay_authors = row['coauthors']
    essay_author = row['author_name']
    
    new_essay = Essay(essay_id, essay_title,essay_authors)

    if head is None:
        head = new_essay  # Set the head of the linked list
        current = head
    else:
        current.next = new_essay  # Link the new essay
        current = new_essay  # Move to the new essay

while head:
    print(head.getAuthors())
    head = head.next
