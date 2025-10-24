from flask import Flask, request, jsonify

app = Flask(__name__)

def add(a, b):
    return a + b

@app.route("/health")
def health():
    return jsonify(status="ok")

@app.route("/sum")
def suma():
    a = int(request.args.get("a", 0))
    b = int(request.args.get("b", 0))
    return jsonify(result=add(a, b))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
