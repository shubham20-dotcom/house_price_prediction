**House Price Prediction Web App 🏡💰**

This is a Flask-based web application that predicts house prices based on user-inputted features:

- **Bedrooms**
- **Bathrooms**
- **Square Footage**

**Features 🚀**

✅ Simple web form to input house details
✅ Uses a trained **Machine Learning model** to predict house prices
✅ Includes **CSS styling** via style.css for a better user experience
✅ Uses **Pipfile** for dependency management
✅ Includes **house\_data.csv** as the dataset

-----
**Setup & Installation 🔧**

**1. Clone the Repository**

git clone https://github.com/yourusername/house-price-prediction.git

cd house-price-prediction

**2. Install Dependencies**

If using **pipenv**:

pip install pipenv

pipenv install

OR using **pip**:

pip install -r requirements.txt

**3. Run the Flask Application**

python app.py

The app will be available at [**http://127.0.0.1:5000/**](http://127.0.0.1:5000/) 🎉

-----
**Usage 🏠**

1. Open your web browser and go to http://127.0.0.1:5000/
1. Enter the house details: 
   1. **Number of bedrooms**
   1. **Number of bathrooms**
   1. **Square footage**
1. Click "Predict" to get the estimated house price
-----
**Project Structure 💽**

house-price-prediction/

|── templates/

|   ├── index.html  # HTML Form for User Input

|── static/

|   ├── style.css   # CSS Styling for the web app

|── data/

|   ├── house\_data.csv  # Housing dataset

|── model.pkl       # Trained Machine Learning Model

|── app.py          # Flask Web App

|── Pipfile         # Pipenv dependency manager file

|── requirements.txt # Alternative dependencies file

|── README.md       # Project Documentation

-----
**Example Screenshots 🗀**

(Add screenshots of form submission and prediction result)

-----
**License 📝**

This project is open-source and available under the **MIT License**.

-----

