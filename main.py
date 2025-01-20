from flask import Flask, render_template, jsonify, request

from search import HybridSearcher

app = Flask(__name__)

hybrid_searcher = HybridSearcher(collection_name="startups")

# @app.get("/api/search")
# def search_startup(q: str):
#     return {"result": hybrid_searcher.search(text=q)}

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/search", methods=["GET"])
def search():
    query = request.args.get("q")
    city = request.args.get("city")
    result = hybrid_searcher.search(text=query, city=city)
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
