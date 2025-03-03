from flask import Flask, render_template, request
import numpy as np
import pickle

app = Flask(__name__)

# Load trained model
with open("model.pkl", "rb") as model_file:
    model = pickle.load(model_file)

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    if request.method == "POST":
        try:
            bedrooms = float(request.form["bedrooms"])
            bathrooms = float(request.form["bathrooms"])
            sqft = float(request.form["sqft"])
            features = np.array([[bedrooms, bathrooms, sqft]])
            prediction = model.predict(features)[0]
        except ValueError:
            prediction = "Invalid input. Please enter numeric values."
    
    return render_template("index.html", prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True)
