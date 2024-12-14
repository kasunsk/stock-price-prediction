# File: predict.py

import numpy as np
import joblib

def predict_next_month(ticker, current_price):
    """Load the trained model for a stock and predict the next month's price."""
    model_path = f"models/{ticker}_linear_regression.pkl"
    model = joblib.load(model_path)
    print(f"Model for {ticker} loaded successfully.")
    prediction = model.predict(np.array([[current_price]]))
    return prediction[0]

# Example usage:
# ticker = "META"
# current_price = 300
# predicted_price = predict_next_month(ticker, current_price)
# print(f"Predicted Price for {ticker} in the next month: {predicted_price}")