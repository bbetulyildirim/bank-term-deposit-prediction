# Bank Term Deposit Prediction

This project predicts whether a client will subscribe to a bank term deposit based on direct marketing campaign data.

## Overview
We trained a machine learning model using the Bank Marketing Dataset from the UCI Machine Learning Repository. The project follows all machine learning pipeline steps, including data cleaning, preprocessing, feature selection, model training, hyperparameter tuning, and deployment via Streamlit.

You can access the live demo here:  
👉 [https://bank-term-deposit-prediction.streamlit.app/](https://bank-term-deposit-prediction.streamlit.app/)

---

## Files
- `app.py`: Streamlit app source code.
- `final_model.pkl`: Trained Random Forest model.
- `bank-additional.csv`: Dataset used for model training.
- `requirements.txt`: List of Python packages required to run the app.

---

## How to Run Locally
If you want to run the application on your local machine:

1. Install Python 3.8+.
2. Install the required libraries:
    ```
    pip install -r requirements.txt
    ```
3. Run the app:
    ```
    streamlit run app.py
    ```
4. The app will open in your browser at `http://localhost:8501`.

---

## Dataset Source
- [UCI Bank Marketing Dataset](https://archive.ics.uci.edu/ml/datasets/Bank+Marketing)

---

## Project Pipeline Summary
- Data Cleaning: Handled missing values (`unknown`) without dropping.
- Data Preprocessing: Encoded categorical variables manually.
- Feature Selection: 20 features were selected for model input.
- Model Selection: Compared Logistic Regression, Random Forest, and Gradient Boosting; selected Random Forest based on evaluation metrics.
- Hyperparameter Tuning: Used GridSearchCV for optimal Random Forest parameters.
- Deployment: Deployed the final model via Streamlit Cloud.

---
