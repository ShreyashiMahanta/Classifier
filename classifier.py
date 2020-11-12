from flask import Flask, Request, jsonify
from controller import getPrediction

app = Flask(__name__)

@app.route("/prediction", methods=["POST"])

def predictData():
    image = request.json.get("image")
    pred = getPrediction(image)
    return jsonify({
        "prediction" : prediction
    },200)

if name == "__main__":
    app.run(debug)