import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
import os

# model_path = os.path.join(os.path.join(os.getcwd(), "data"), "model.pkl")
# template_folder = os.path.join(os.path.join(os.getcwd(), "templates"))

# model_path = ".\data\model.pkl"
# template_folder = ".\\templates"

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
model_path = os.path.join(BASE_DIR, 'model.pkl')
template_folder = os.path.join(BASE_DIR, 'templates')


app = Flask(__name__, template_folder = template_folder)
# app.debug= True
model = pickle.load(open(model_path, 'rb'))


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=['POST'])
def predict():
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]

    prediction = model.predict(final_features)
    output = round(prediction[0], 2)

    return render_template("index.html", prediction_text="Salary should be {}".format(output))


@app.route("/results", methods=['POST'])
def results():
    data = request.get_json(force=True)
    prediction = model.predict([np.array(list(data.values()))])

    output = prediction[0]
    return jsonify(output)


if __name__ == "__main__":
    app.run()