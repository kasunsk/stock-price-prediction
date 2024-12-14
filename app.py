# File: app.py

from flask import Flask, request, render_template
from scripts.train_model import fetch_stock_data, preprocess_data, train_model
from scripts.predict import predict_next_month
import os
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/train', methods=['POST'])
def train():
    ticker = request.form['ticker']
    start_date = request.form['start_date']
    end_date = request.form['end_date']

    # Fetch and preprocess data
    stock_data = fetch_stock_data(ticker, start_date, end_date)
    processed_data = preprocess_data(stock_data)

    # Train the model
    train_model(ticker, processed_data)
    return f"Model for {ticker} trained successfully!"

@app.route('/predict', methods=['POST'])
def predict():
    ticker = request.form['ticker']
    current_price = float(request.form['current_price'])

    # Predict next month's price
    predicted_price = predict_next_month(ticker, current_price)
    return f"Predicted price for {ticker} in the next month: {predicted_price}"

if __name__ == '__main__':
    if not os.path.exists('models'):
        os.makedirs('models')
    app.run(debug=True)
