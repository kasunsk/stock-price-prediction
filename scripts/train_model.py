# File: train_model.py

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import joblib
import yfinance as yf
import pandas as pd

def fetch_stock_data(ticker, start_date, end_date):
    """Fetch stock data from Yahoo Finance for a given ticker."""
    print(f"Fetching data for {ticker}...")
    stock_data = yf.download(ticker, start=start_date, end=end_date)
    return stock_data

def fetch_current_stock_price(ticker, start_date, end_date):
    """
    Fetch stock data from Yahoo Finance for a given ticker.
    If data is not available for the given range, check for previous dates iteratively.
    """
    print(f"Fetching data for {ticker} from {start_date} to {end_date}...")

    while True:
        # Try fetching data for the specified range
        stock_data = yf.download(ticker, start=start_date, end=end_date)

        if not stock_data.empty:
            print(f"Data found for {ticker} from {start_date} to {end_date}.")
            # Backfill and forward-fill missing data
            stock_data = stock_data.ffill().bfill()  # Fill NaNs with forward and backward fill
            return stock_data

        # If data is empty, move the start_date and end_date backward by 1 day
        print(f"No data found for {ticker} from {start_date} to {end_date}. Checking previous dates...")
        start_date = (pd.Timestamp(start_date) - pd.Timedelta(days=1)).strftime('%Y-%m-%d')
        end_date = (pd.Timestamp(end_date) - pd.Timedelta(days=1)).strftime('%Y-%m-%d')

        # If we go too far back (e.g., past 10 years), raise an error
        if pd.Timestamp(start_date) < pd.Timestamp("2000-01-01"):
            raise ValueError(f"No stock data available for {ticker} before 2000-01-01.")

def preprocess_data(data):
    """Preprocess stock data for training and testing."""
    data['Day Number'] = (data.index - data.index[0]).days  # Days since the start
    data['Future Price'] = data['Close'].shift(-30)
    data.dropna(inplace=True)
    return data

def train_model(ticker, data):
    """Train and save a Linear Regression model for a specific stock ticker."""
    X = data[['Close', 'Day Number']]  # Include 'Day Number' as a feature
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