#Import Libraries
import numpy as np
import pandas as pd
import joblib
 
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
 
#load data
df = pd.read_csv(r"C:\Users\anujm\OneDrive\Desktop\CODING\Machine Learning\Banglore House Prediction\BHP_Cleaned_Data.csv")
 
# Split data
X= df.drop('price', axis=1)
y= df['price']
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.2, random_state=51)
 
# feature scaling
sc = StandardScaler()
sc.fit(X_train)
X_train = sc.transform(X_train)
X_test = sc.transform(X_test)
 
 
###### Load Model
 
model = joblib.load(r"C:\Users\anujm\OneDrive\Desktop\CODING\Machine Learning\Banglore House Prediction\bangalore_house_price_prediction_rfr_model.pkl")
 
 
# it help to get predicted value of house  by providing features value 
def predict_house_price(size_bhk, total_sqft, bath, balcony, price_per_sqft, availability, area_type, location):
    x = np.zeros(len(X.columns))  # X.columns comes from your loaded DataFrame

    # Set main features by their column index
    x[X.columns.get_loc('size_bhk')] = size_bhk
    x[X.columns.get_loc('total_sqft')] = total_sqft
    x[X.columns.get_loc('bath')] = bath
    x[X.columns.get_loc('balcony')] = balcony
    x[X.columns.get_loc('price_per_sqft')] = price_per_sqft
    x[X.columns.get_loc('availability')] = availability  # 0 or 1

    # Set area_type one-hot
    area_col = f'area_type_{area_type}'
    if area_col in X.columns:
        x[X.columns.get_loc(area_col)] = 1

    # Set location one-hot
    loc_col = f'location_{location}'
    if loc_col in X.columns:
        x[X.columns.get_loc(loc_col)] = 1

    # Feature scaling
    x = sc.transform([x])[0]

    return model.predict([x])[0]


# Its just a test case to run this file independently and check the output if needed
if __name__ == "__main__":
    # Example values (replace with realistic ones from your data)
    size_bhk = 2
    total_sqft = 1056
    bath = 2
    balcony = 1
    price_per_sqft = 3699.81
    availability = 0  # 1 or 0 as per your data
    area_type = "Super built-up  Area"  # must match one-hot column suffix
    location = "Electronic City Phase II"       # must match one-hot column suffix

    predicted_price = predict_house_price(
        size_bhk, total_sqft, bath, balcony, price_per_sqft, availability, area_type, location
    )
    print("Predicted price:", predicted_price)
