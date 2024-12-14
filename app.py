# File: app.py

from flask import Flask, request, render_template, jsonify
from scripts.train_model import fetch_stock_data, preprocess_data, train_model
from scripts.predict import predict_next_month, predict_next_30_days
import os

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
    return jsonify({'message': f'Model for {ticker} trained successfully!'})

@app.route('/predict', methods=['POST'])
def predict():
    ticker = request.form['ticker']
    current_price = float(request.form['current_price'])

    # Predict next month's price
    predicted_price = predict_next_month(ticker, current_price)
    return f"Predicted price for {ticker} in the next month: {predicted_price}"

@app.route('/current_price', methods=['POST'])
def get_current_price():
    ticker = request.json.get('ticker')
    end_date = request.json.get('end_date')

    # Fetch stock data for the given date
    stock_data = fetch_stock_data(ticker, end_date, end_date)

    if stock_data.empty:
        return jsonify({'error': 'No data found for the selected date.'}), 400

    # Extract the 'Close' price as a single float value
    current_price = stock_data['Close'].iloc[-1]
    current_price = round(float(current_price), 2)   # Ensure it is JSON serializable
    return jsonify({'current_price': current_price})

@app.route('/predict_30_days', methods=['POST'])
def predict_30_days():
    ticker = request.json.get('ticker')
    current_price = float(request.json.get('current_price'))

    # Predict the next 30 days' prices
    prediction_data = predict_next_30_days(ticker, current_price)
    return jsonify(prediction_data)


if __name__ == '__main__':
    if not os.path.exists('models'):
        os.makedirs('models')
    app.run(debug=True)
