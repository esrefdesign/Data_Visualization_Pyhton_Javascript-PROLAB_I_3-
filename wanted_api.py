from flask import Flask, request, jsonify,render_template
from main import unique_authors, unique_essasys,graph
from isterler import Wanted
from flask_cors import CORS

app = Flask(__name__, 
            static_url_path="",
            static_folder="web",
            )
# Flask route for wanted_5 function

CORS(app)

@app.route('/get_graph',methods=['GET'])
def get_graph():
     # Nodes ve Edges dizileri
    nodes = [
        {
            "name": author,
            "size": graph.get_node_size(author),
        }
        for author in graph.adj_list.keys()
    ]
    edges = [
        {
            "source": author1,
            "target": author2,
        }
        for author1 in graph.adj_list
        for author2 in graph.adj_list[author1]
        if author1 < author2  # Kenarları çift yazmamak için
    ]

    # JSON olarak döndür
    return jsonify({"nodes": nodes, "edges": edges})

@app.route('/wanted_1', methods=['POST'])
def wanted_1():
    print("1. Endpoint'e giriş yapıldı.")
    data = request.json
    author_A = data.get('author_A')
    author_B = data.get('author_B')

    if not author_A or not author_B:
        return jsonify({"error": "Both author_A and author_B are required"}), 400

    wanteds = Wanted(graph, unique_authors, unique_essasys)
    result = wanteds.wanted_1(author_A, author_B)
    return jsonify({"data": result}), 200

@app.route('/wanted_2', methods=['POST'])
def wanted_2():
    print("2. Endpoint'e giriş yapıldı.") 

    data = request.json.get('author_name')  # Kullanıcıdan alınan A yazarının ID'si
    if not data:
        return jsonify({"error": "Author ID is required"}), 400
    wanteds = Wanted(graph,unique_authors,unique_essasys)
    result = wanteds.wanted_2(data)
    return jsonify({"priority_queue":result}),200

@app.route('/wanted_3', methods=['POST'])
def wanted_3():
    print("3. Endpoint'e giriş yapıldı.")
    data = request.json
    author_name = data.get('author_name')

    if not author_name:
        return jsonify({"error": "Author name is required"}), 400

    wanteds = Wanted(graph, unique_authors, unique_essasys)
    result = wanteds.wanted_3(author_name)
    return jsonify({"data": result,}), 200

@app.route('/wanted_4', methods=['POST'])
def wanted_4():
    print("4. Endpoint'e giriş yapıldı.")
    author_name = request.json.get('author_name')  # Kullanıcıdan alınan A yazarının ID'si
    if not author_name:
        return jsonify({"error": "Author ID is required"}), 400
    wanteds = Wanted(graph, unique_authors, unique_essasys)
    result = wanteds.wanted_4(author_name)
    return jsonify({"distance_table": result}), 200

@app.route('/wanted_5', methods=['POST'])

def wanted_5():
    print("5. Endpoint'e giriş yapıldı.") 
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

@app.route('/wanted_7', methods=['POST'])
def wanted_7():
    print("7. Endpoint'e giriş yapıldı.")
    author_name = request.json.get('author_name')  # Kullanıcıdan alınan A yazarının adı
    if not author_name:
        return jsonify({"error": "Author name is required"}), 400  # Yazar adı zorunlu

    wanteds = Wanted(graph, unique_authors, unique_essasys)
    result = wanteds.wanted_7(author_name)
    return jsonify(result), 200

if __name__ == '__main__':
    app.run(debug=True)