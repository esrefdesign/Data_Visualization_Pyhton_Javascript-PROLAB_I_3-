from flask import Flask, request, jsonify
from main import unique_authors, unique_essasys
from isterler import Wanted
from flask_cors import CORS
app = Flask(__name__, 
            static_url_path="",
            static_folder="web"
            )
# Flask route for wanted_5 function

CORS(app)
@app.route('/wanted_5', methods=['POST'])

def wanted_5():
    print("Endpoint'e giriş yapıldı.") 
    author_name = request.json.get('author_name')
    if not author_name:
        return jsonify({"error": "author_name is required"}), 400  # Hatalı durum için
    wanteds = Wanted(unique_authors, unique_essasys)
    result = wanteds.wanted_5(author_name)
    return jsonify({"coauthor_count": result}),200



if __name__ == '__main__':
    app.run(debug=True)