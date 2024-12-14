# File: predict.py

import numpy as np
import joblib
import pandas as pd

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

def predict_next_30_days(ticker, current_price):
    """Load the trained model for a stock and predict the next 30 days' prices."""
    model_path = f"models/{ticker}_linear_regression.pkl"
    model = joblib.load(model_path)
    print(f"Model for {ticker} loaded successfully.")

    predictions = []
    for day in range(30):
        next_price = model.predict(np.array([[current_price]]))[0]
        predictions.append(next_price)
        current_price = next_price  # Update current_price for the next prediction

    # Generate dates for the next 30 days
    dates = pd.date_range(start=pd.Timestamp.today(), periods=30).strftime('%Y-%m-%d').tolist()
    return {'dates': dates, 'prices': predictions}