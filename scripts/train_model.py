# File: train_model.py

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import joblib

# Load the dataset
data = pd.read_csv("data/stock_data.csv")

# Preprocess the data
data['Date'] = pd.to_datetime(data['Date'])
data.set_index('Date', inplace=True)
data['Future Price'] = data['Close'].shift(-1)
data.dropna(inplace=True)

# Define features and labels
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
print(f"Mean Squared Error: {mse}")

# Save the trained model
joblib.dump(model, "models/linear_regression.pkl")
print("Model saved as models/linear_regression.pkl")