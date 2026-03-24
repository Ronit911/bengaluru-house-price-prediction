import pandas as pd
from typing import Tuple, Optional

def create_input_dataframe(location: str, sqft: float, bath: int, bhk: int) -> pd.DataFrame:
    """
    Creates a pandas DataFrame from input features for model prediction.

    Args:
        location: The area in Bengaluru.
        sqft: Total area in square feet.
        bath: Number of bathrooms.
        bhk: Number of bedrooms.

    Returns:
        A pandas DataFrame with a single row of features.
    """
    return pd.DataFrame({
        'location': [location],
        'total_sqft': [sqft],
        'bath': [bath],
        'bhk': [bhk]
    })


def validate_input(location: str, sqft: float, bath: int, bhk: int) -> Tuple[bool, Optional[str]]:
    """
    Validates user input for house features.

    Args:
        location: The area in Bengaluru.
        sqft: Total area in square feet.
        bath: Number of bathrooms.
        bhk: Number of bedrooms.

    Returns:
        A tuple of (is_valid, error_message).
    """
    if sqft <= 0 or bath <= 0 or bhk <= 0:
        return False, "Values must be greater than zero"

    if bath > bhk + 2:
        return False, "Unrealistic bathroom count (bath > bhk + 2)"

    if not location or location.strip() == "":
        return False, "Location cannot be empty"

    return True, None