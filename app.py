from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

# Load trained model and scaler
model = joblib.load("iris_model.joblib")
scaler = joblib.load("iris_scaler.joblib")

# Mapping from prediction to species name
species_map = {0: "setosa", 1: "versicolor", 2: "virginica"}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Get user inputs
        sepal_length = float(request.form["sepal_length"])
        sepal_width = float(request.form["sepal_width"])
        petal_length = float(request.form["petal_length"])
        petal_width = float(request.form["petal_width"])
        
        # Create numpy array for model
        user_input = np.array([[sepal_length, sepal_width, petal_length, petal_width]])

        # Scale input
        scaled_input = scaler.transform(user_input)

        # Predict species
        prediction_index = model.predict(scaled_input)[0]
        prediction = species_map[prediction_index]

        return render_template("result.html", prediction=prediction)
    
    except ValueError:
        return render_template("result.html", prediction="Invalid input")

if __name__ == "__main__":
    app.run(debug=True)
