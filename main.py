# File: main.py

from scripts.train_model import fetch_stock_data, preprocess_data, train_model
from scripts.predict import predict_next_month

# Example workflow
if __name__ == "__main__":
    tickers = ["META", "TSLA", "IBKR", "AAPL", "AMZN", "S63.SI", "Z74.SI"]
    start_date = "2020-01-01"
    end_date = "2024-11-30"

    # Fetch data
    stock_data = fetch_stock_data(tickers, start_date, end_date)

    # Preprocess data
    processed_data = preprocess_data(stock_data)

    # Train models for each stock
    for ticker, data in processed_data.items():
        train_model(ticker, data)

    # Predict the next month's price for a specific stock
    ticker = "META"
    current_price = 580  # Replace with the latest close price
    predicted_price = predict_next_month(ticker, current_price)
    print(f"Predicted Price for {ticker} in the next month: {predicted_price}")

    # Predict the next month's price for a specific stock
    ticker2 = "TSLA"
    current_price = 345  # Replace with the latest close price
    predicted_price = predict_next_month(ticker2, current_price)
    print(f"Predicted Price for {ticker2} in the next month: {predicted_price}")