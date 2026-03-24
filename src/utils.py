def format_price(price: float) -> str:
    """
    Formats the price in Lakhs or Crores.

    Args:
        price: Price in Lakhs.

    Returns:
        A formatted string (e.g., '1.50 Crores' or '50.00 Lakhs').
    """
    if price >= 100:
        return f"{price/100:.2f} Crores"
    return f"{price:.2f} Lakhs"


def price_category(price: float) -> str:
    """
    Categorizes the house price into Budget, Mid-range, or Premium.

    Args:
        price: Price in Lakhs.

    Returns:
        Category string.
    """
    if price < 50:
        return "Budget"
    elif price < 150:
        return "Mid-range"
    else:
        return "Premium"