# File: predict.py

import pandas as pd
import numpy as np
import joblib

# Load the trained model
model = joblib.load("models/linear_regression.pkl")
print("Model loaded successfully.")

# Predict the next day price
def predict_next_day(current_price):
    prediction = model.predict(np.array([[current_price]]))
    return prediction[0]

# Example usage
current_price = 100  # Replace with the latest closing price
predicted_price = predict_next_day(current_price)
print(f"Predicted Price for the Next Day: {predicted_price}")