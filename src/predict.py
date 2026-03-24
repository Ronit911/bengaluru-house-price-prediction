import pickle
import pandas as pd
from src.preprocess import create_input_dataframe

# Load model from the correct path
MODEL_PATH = 'model/RidgeModel.pkl'
with open(MODEL_PATH, 'rb') as f:
    model = pickle.load(f)


def predict_price(location: str, sqft: float, bath: int, bhk: int) -> float:
    """
    Predicts the house price in Bengaluru based on input features.

    Args:
        location: The area in Bengaluru.
        sqft: Total area in square feet.
        bath: Number of bathrooms.
        bhk: Number of bedrooms.

    Returns:
        The predicted price in Lakhs.
    """
    input_df = create_input_dataframe(location, sqft, bath, bhk)
    prediction = model.predict(input_df)[0]
    return float(prediction)