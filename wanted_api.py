from flask import Flask, request, jsonify
from main import unique_authors, unique_essasys,graph
from isterler import Wanted
from flask_cors import CORS
app = Flask(__name__, 
            static_url_path="",
            static_folder="web"
            )
# Flask route for wanted_5 function

CORS(app)

@app.route('/wanted_2', methods=['POST'])
def wanted_2():
    data = request.json
    author_id = data.get('author_id')  # Kullanıcıdan alınan A yazarının ID'si
    if not author_id:
        return jsonify({"error": "Author ID is required"}), 400

    # A yazarını bul ve işbirliği yaptığı yazarları listele
    author = next((a for a in unique_authors.values() if a.ID == author_id), None)
    if not author:
        return jsonify({"error": "Author not found"}), 404

    # İşbirliği yaptığı yazarlar ve düğüm ağırlıklarını hesapla
    collaborators = []
    for collaborator_name in graph.adj_list.get(author.name, []):
        collaborator = unique_authors[collaborator_name]
        weight = len(collaborator.essay)  # Makale sayısı düğüm ağırlığı olarak alınır
        collaborators.append({"name": collaborator.name, "weight": weight})

    # Düğüm ağırlıklarına göre sıralama
    collaborators.sort(key=lambda x: x["weight"], reverse=True)
    return jsonify(collaborators)

@app.route('/wanted_5', methods=['POST'])

def wanted_5():
    print("Endpoint'e giriş yapıldı.") 
    author_name = request.json.get('author_name')
    if not author_name:
        return jsonify({"error": "author_name is required"}), 400  # Hatalı durum için
    wanteds = Wanted(graph,unique_authors, unique_essasys)
    result = wanteds.wanted_5(author_name)
    return jsonify({"coauthor_count": result}),200

@app.route('/wanted_6', methods=['POST'])

def wanted_6():
    print("6. enpoint")
    wanteds=Wanted(graph,unique_authors,unique_essasys)
    return jsonify(wanteds.wanted_6())

if __name__ == '__main__':
    app.run(debug=True)