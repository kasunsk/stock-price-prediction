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

def predict_next_6_months(ticker, current_price):
    """Predict weekly average stock prices for the next 6 months."""
    model_path = f"models/{ticker}_linear_regression.pkl"
    model = joblib.load(model_path)
    print(f"Model for {ticker} loaded successfully.")

    predictions = []
    weeks = []
    current_week_price_sum = 0
    current_week_days = 0
    week_count = 1

    for day in range(180):  # 6 months = ~180 days
        next_price = model.predict(np.array([[current_price]]))[0]
        current_price = next_price
        current_week_price_sum += next_price
        current_week_days += 1

        if (day + 1) % 7 == 0:  # End of the week
            avg_week_price = current_week_price_sum / current_week_days
            predictions.append(avg_week_price)
            weeks.append(f"Week {week_count}")
            current_week_price_sum = 0
            current_week_days = 0
            week_count += 1

    return {'weeks': weeks, 'prices': predictions}
