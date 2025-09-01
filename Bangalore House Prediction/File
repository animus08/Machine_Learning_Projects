#Import Libraries
from flask import Flask, request, render_template

import model  # load model.py
from model import X

# Read locations from your DataFrame columns
locations = [col.replace('location_', '') for col in X.columns if col.startswith('location_')]
area_types = [col.replace('area_type_', '') for col in X.columns if col.startswith('area_type_')]

app = Flask(__name__)
 
# render htmp page
@app.route('/')
def home():
    return render_template('index.html', locations=locations, area_types=area_types)
 
# get user input and the predict the output and return to user
@app.route('/predict',methods=['POST'])
def predict():
    # take data from form and store in each feature    
    input_features = [x for x in request.form.values()]
    size_bhk = float(input_features[0])
    total_sqft = float(input_features[1])
    bath = float(input_features[2])
    balcony = float(input_features[3])
    price_per_sqft = float(input_features[4])
    availability = int(input_features[5])  # should be 0 or 1
    area_type = input_features[6]
    location = input_features[7]

    # predict the price of house by calling model.py
    predicted_price = model.predict_house_price(
        size_bhk, total_sqft, bath, balcony, price_per_sqft, availability, area_type, location
    )
    rounded_price = round(predicted_price, 2)
    prediction_text = f"Predicted Price of Bangalore House is {rounded_price} Lakhs"
    return render_template('index.html', prediction_text=prediction_text, locations=locations, area_types=area_types)
 
# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port="8080")
     
if __name__ == "__main__":
    app.run()
