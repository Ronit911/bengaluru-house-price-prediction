import pandas as pd
import logging
from flask import Flask, request, render_template, jsonify
from src.predict import predict_price
from src.utils import format_price, price_category
from src.preprocess import validate_input

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

app = Flask(__name__)

# Load unique locations once at startup
try:
    df = pd.read_csv('data/Clean_data.csv')
    LOCATIONS = sorted(df['location'].unique().tolist())
    logger.info(f"Loaded {len(LOCATIONS)} unique locations.")
except Exception as e:
    logger.warning(f"Error loading locations: {e}. Using empty list.")
    LOCATIONS = []


@app.route('/')
def home():
    return render_template('index.html', locations=LOCATIONS)


@app.route('/predict', methods=['POST'])
def predict():
    try:
        location = request.form['location']
        sqft = float(request.form['sqft'])
        bath = int(request.form['bath'])
        bhk = int(request.form['bhk'])

        valid, error = validate_input(location, sqft, bath, bhk)

        if not valid:
            return render_template('index.html', prediction_text=error, locations=LOCATIONS)

        price = predict_price(location, sqft, bath, bhk)

        formatted_price = format_price(price)
        category = price_category(price)

        result = f"{formatted_price} ({category})"
        logger.info(f"Prediction for {location}, {sqft}sqft: {result}")

        return render_template('index.html', prediction_text=result, locations=LOCATIONS)
    except Exception as e:
        logger.error(f"Error during prediction: {e}")
        return render_template('index.html', prediction_text="An error occurred. Please check your inputs.", locations=LOCATIONS)


# 🔥 API endpoint (IMPORTANT FOR RESUME)
@app.route('/predict_api', methods=['POST'])
def predict_api():
    data = request.get_json()

    price = predict_price(
        data['location'],
        data['total_sqft'],
        data['bath'],
        data['bhk']
    )

    return jsonify({
        "predicted_price_lakhs": round(price, 2),
        "category": price_category(price)
    })


if __name__ == "__main__":
    app.run(debug=True)