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
    data = request.json.get('author_name')  # Kullanıcıdan alınan A yazarının ID'si
    if not data:
        return jsonify({"error": "Author ID is required"}), 400
    wanteds = Wanted(graph,unique_authors,unique_essasys)
    result = wanteds.wanted_2(data)
    return jsonify({"priority_queue":result}),200
  

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