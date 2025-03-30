# Iris Flower Classification Web App

This is a **Machine Learning Web Application** that predicts the species of an Iris flower based on user input measurements. The model is built using **Logistic Regression**, and the web interface is developed using **Flask**.

---

## 📌 Features
- Predicts the Iris flower species (**Setosa, Versicolor, or Virginica**) based on sepal and petal measurements.
- User-friendly **web interface** built with Flask.
- Scikit-learn **Logistic Regression model** for classification.
- Displays an image of the predicted flower species.

---

## 🛠️ Technologies Used
- **Python**
- **Flask** (for web development)
- **Scikit-learn** (for machine learning model)
- **HTML, CSS, Bootstrap** (for frontend design)
- **Joblib** (for model serialization)

---

## 📂 Project Structure
```
├── static/
│   ├── css/
│   │   ├── style.css
│   ├── images/
│       ├── setosa.jpg
│       ├── versicolor.jpg
│       ├── virginica.jpg
├── templates/
│   ├── index.html
│   ├── result.html
├── iris_model.joblib  # Saved ML model
├── iris_scaler.joblib # Scaler for input normalization
├── train.py           # Script to train and save the model
├── app.py             # Flask web application
├── README.md          # Documentation
├── requirements.txt   # Dependencies
```

---

## 🚀 Installation & Setup

### 1️⃣ Install Required Dependencies
First, install **Python** (if not already installed). Then, install the required libraries:
```sh
pip install -r requirements.txt
```

### 2️⃣ Train the Model (Optional)
If you want to retrain the model, run:
```sh
python train.py
```

### 3️⃣ Run the Flask Web App
Start the web application using:
```sh
python app.py
```
The app will be accessible at:  
👉 **http://127.0.0.1:5000/**

---

## 🎨 How It Works
1. Open the **web app** in your browser.
2. Enter the **sepal length, sepal width, petal length, and petal width**.
3. Click the **Predict** button.
4. The app will display:
   - The **predicted species** name.
   - An **image** of the predicted flower.

---

## 🖼️ Screenshots
### 🔹 Home Page
![Home Page](static/images/homepage.png)

### 🔹 Prediction Result
![Result Page](static/images/resultpage.png)

---

## 🛠️ Troubleshooting
- If the **CSS is not loading**, ensure the `static/` folder is correctly linked in your HTML:
  ```html
  <link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">
  ```
- If **images do not appear**, check the file paths in `result.html`:
  ```html
  <img src="{{ url_for('static', filename='images/' + image_filename) }}" alt="Flower Image">
  ```

---

## 📌 Future Improvements
✅ Deploy to **Heroku** or **GitHub Pages**
✅ Improve UI with **Bootstrap and JavaScript**
✅ Add **more ML models** for comparison

---

## 📜 License
This project is **open-source** and available under the **MIT License**.

---

## 💡 Author
Developed by **Jeetash Goswami** 🚀
