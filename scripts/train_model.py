# File: train_model.py

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import joblib
import yfinance as yf

def fetch_stock_data(ticker, start_date, end_date):
    """Fetch stock data from Yahoo Finance for a given ticker."""
    print(f"Fetching data for {ticker}...")
    stock_data = yf.download(ticker, start=start_date, end=end_date)
    return stock_data

def preprocess_data(data):
    """Preprocess stock data for training and testing."""
    data['Future Price'] = data['Close'].shift(-30)
    data.dropna(inplace=True)
    return data

def train_model(ticker, data):
    """Train and save a Linear Regression model for a specific stock ticker."""
    X = data[['Close']]
    y = data['Future Price']

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train the model
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Evaluate the model
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    print(f"[{ticker}] Mean Squared Error: {mse}")

    # Save the trained model
    joblib.dump(model, f"models/{ticker}_linear_regression.pkl")
    print(f"Model saved as models/{ticker}_linear_regression.pkl")