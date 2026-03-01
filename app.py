import pandas as pd
from flask import Flask, render_template, request
import pickle

app = Flask(__name__)
data = pd.read_csv('data/Clean_data.csv')
pipe = pickle.load(open('model/RidgeModel.pkl','rb'))


def format_price(price_lakh):
    if price_lakh >= 100:
        return f" {price_lakh/100:.2f} Cr"
    else:
        return f" {price_lakh:.2f} Lakhs"


@app.route('/')
def index():
    locations = sorted(data['location'].unique())
    return render_template('index.html', locations=locations)


@app.route('/predict', methods=['POST'])
def predict():

    try:
        location = request.form.get('location')
        bhk = int(request.form.get('BHK'))
        bath = float(request.form.get('bath'))
        sqft = float(request.form.get('total_sqft'))

        input_df = pd.DataFrame({
            'location':[location],
            'total_sqft':[sqft],
            'bath':[bath],
            'bhk':[bhk]
        })

        prediction = pipe.predict(input_df)[0]

        formatted_price = format_price(prediction)

        return formatted_price

    except Exception as e:
        print("ERROR:", e)
        return str(e)


if __name__ == '__main__':
    app.run(debug=True)