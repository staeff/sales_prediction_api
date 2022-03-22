import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
import os

app = Flask(__name__)
model = pickle.load(open("data/model.pkl", "rb"))


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)

    output = round(prediction[0], 2)

    return render_template(
        "index.html", prediction_text=f"Sales should be $ {output}"
    )


@app.route("/results", methods=["POST"])
def results():

    data = request.get_json(force=True)
    prediction = model.predict([np.array(list(data.values()))])

    output = prediction[0]
    return jsonify(output)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
