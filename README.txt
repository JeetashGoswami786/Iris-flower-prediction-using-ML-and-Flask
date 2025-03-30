Iris Flower Classification Web Application

Overview:
This project is a machine learning-based web application that predicts the species of an Iris flower based on user-inputted measurements. It uses Logistic Regression trained on the Iris dataset and is deployed as a web application using Flask.

Features:
- Users can input sepal length, sepal width, petal length, and petal width.
- The model predicts the species: Setosa, Versicolor, or Virginica.
- A corresponding image of the predicted flower is displayed.
- Built using Flask, Scikit-learn, Joblib, Bootstrap, and HTML/CSS.

Requirements:
Ensure you have Python installed. Install the necessary dependencies using:
```
pip install -r requirements.txt
```
Required Libraries:
- Flask
- Scikit-learn
- Numpy
- Joblib

Project Structure:
```
/iris_flask_app
│── /static
│   ├── /css
│   │   ├── styles.css
│   ├── /images
│   │   ├── setosa.jpg
│   │   ├── versicolor.jpg
│   │   ├── virginica.jpg
│── /templates
│   ├── index.html
│   ├── result.html
│── iris_model.joblib
│── iris_scaler.joblib
│── app.py
│── train.py
│── README.txt
│── requirements.txt
```

How to Train the Model:
To train the model and save it for later use, run:
```
python train.py
```
This script:
1. Loads the Iris dataset.
2. Scales the features using StandardScaler.
3. Trains a Logistic Regression model.
4. Saves the trained model (iris_model.joblib) and scaler (iris_scaler.joblib).

Running the Web Application:
1. Start Flask Server:
```
python app.py
```
2. Open your browser and visit:
```
http://127.0.0.1:5000/
```

Using the Application:
1. Enter four numeric values (sepal length, sepal width, petal length, petal width).
2. Click Predict.
3. The species name and corresponding image will be displayed.
4. Click Make Another Prediction to return to the home page.

Troubleshooting:
- CSS not working? Ensure styles.css is inside the /static/css/ folder and linked correctly in HTML.
- Images not displaying? Make sure images are placed inside /static/images/ and correctly referenced in result.html.
- Invalid input error? Ensure only numeric values are entered in the form.

Future Enhancements:
- Add more advanced ML models like Random Forest or SVM.
- Deploy on Heroku/AWS for online access.
- Improve UI with Bootstrap and JavaScript enhancements.

---
Created by [Your Name]

