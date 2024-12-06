import pandas as pd
from author_node import *;
from essay_node import *;

# Excel'den veriyi çekme
data = pd.read_excel('DATASET.xlsx',nrows=10)

data['coauthors'] = data['coauthors'].apply(lambda x: x.split(',') if x else [])

top_10_data = data.head(10)

# Makale adına göre yardımcı yazarları ekrana basan fonksiyon
def print_co_authors(article_name):
    # Makaleyi bul
    row = top_10_data[top_10_data["paper_title"] == article_name]
    
    if not row.empty:
        co_authors = row.iloc[0]["coauthors"]
        print(f"Makaleye ait yardımcı yazarlar: {', '.join(co_authors) if co_authors else 'Yardımcı yazar yok.'}")
    else:
        print("Makale bulunamadı.")

# Örnek kullanım
article_name_input = input("Makale adını girin: ")
print_co_authors(article_name_input)