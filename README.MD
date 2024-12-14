# File: README.md

# Stock Price Prediction Project

This project demonstrates how to use machine learning to predict stock prices for multiple stocks over the next month based on historical data fetched from Yahoo Finance.

## Features
- Fetch historical stock data for multiple stocks using Yahoo Finance API.
- Train a machine learning model (Linear Regression) for each stock.
- Predict the next month's price for a specific stock.

## File Structure

```
stock-price-prediction/
├── data/
│   └── (Dynamically fetched stock data)
├── notebooks/
│   └── exploration.ipynb       # Jupyter notebook for data exploration (optional)
├── models/
│   └── ticker_model.pkl        # Saved model files for each stock (e.g., META_linear_regression.pkl)
├── train_model.py              # Script for fetching, preprocessing, and training models
├── predict.py                  # Script to load models and make predictions
├── requirements.txt            # List of Python dependencies (e.g., pandas, numpy, scikit-learn, yfinance)
├── README.md                   # Project overview and setup instructions
└── main.py                     # Main script to execute the workflow

## Instructions

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the complete workflow:
   ```bash
   python main.py
   ```

3. Predict for a specific stock:
   ```bash
   python predict.py
   ```

## Requirements
- Python 3.7+
- pandas
- numpy
- scikit-learn
- joblib
- yfinance