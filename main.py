# File: main.py

from scripts.train_model import train_model
from scripts.predict import predict_next_day

# Example workflow
if __name__ == "__main__":
    # Train the model
    train_model()

    # Make predictions
    current_price = 100  # Replace with your input
    predicted_price = predict_next_day(current_price)
    print(f"Predicted Price for the Next Day: {predicted_price}")