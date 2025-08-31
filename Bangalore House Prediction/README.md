# 🏠 Bangalore House Price Prediction

This project is a **machine learning web application** that predicts house prices in Bangalore, India.  
The application uses a **Random Forest Regressor** model trained on a cleaned dataset of real estate properties.  
The web interface is built using **Flask**, allowing users to input various house features and get an estimated price.

---

## ✨ Features

- **Data Cleaning and EDA**:  
  The `Bangalore_House_Prediction_Cleaning.ipynb` notebook details the data cleaning process, including:
  - Handling missing values  
  - Removing duplicates  
  - Feature engineering  
  - Outlier detection and removal (e.g., minimum square feet per BHK, price per square feet)

- **Machine Learning Models**:  
  The `Bangalore_House_Prediction_Model.ipynb` notebook demonstrates training of several regression models:
  - Linear Regression, Lasso, Ridge, Support Vector Machine, Random Forest, and XGBoost  
  - Performance comparison using **R-squared** and **RMSE**  
  - Random Forest Regressor showed the **highest accuracy** and was chosen for deployment

- **Web Application**:  
  - Built with **Python + Flask**  
  - `app.py` handles backend logic, renders HTML, and processes predictions  
  - `index.html` provides a form for input (BHK, square feet, bathrooms, balconies, area type, location)

- **Model Deployment**:  
  - Trained Random Forest model and StandardScaler are saved with **joblib**  
  - Easy loading for real-time predictions in the Flask app

---

## 📂 Project Structure

```

Bangalore\_House\_Prediction/
│── index.html                                               # Front-end HTML form
│── app.py                                                   # Flask app to serve predictions
│── model.py                                                 # Loads model & scaler, predicts prices
│── Bangalore\_House\_Prediction\_Cleaning.ipynb             # Data cleaning & preprocessing
│── Bangalore\_House\_Prediction\_Model.ipynb                # Model training & evaluation
│── BHP\_Cleaned\_Data.csv                                   # Cleaned dataset
│── bengaluru\_house\_price\_prediction\_rfr\_model.pkl      # Trained Random Forest model
│── Bengaluru\_House\_Data.csv                               # Raw dataset

````

---

## ⚙️ How to Run

Clone the repository:

```bash
git clone [your-repository-url]
cd Bangalore_House_Prediction
````

Install dependencies:

```bash
pip install Flask scikit-learn numpy pandas joblib
```

Run the Flask app:

```bash
python app.py
```

Open in your browser:

👉 [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 📊 Model Performance

| Model                  | R² Score  | RMSE     |
| ---------------------- | --------- | -------- |
| Linear Regression      | 0.939     | 18.02    |
| Lasso                  | 0.936     | 18.50    |
| Support Vector Machine | 0.503     | 51.53    |
| **Random Forest**      | **0.996** | **4.61** |
| XGBoost                | 0.994     | 5.71     |

✅ Random Forest achieved the **best performance**.

---

## 🧹 Data Cleaning Insights

* **Missing Values**:

  * `society` column dropped (41.3% missing)
  * `balcony` filled with median
  * Rows with missing `location` and `size` dropped (few in number)

* **Feature Engineering**:

  * Created `size_bhk` (number of bedrooms extracted from `size`)
  * Cleaned `total_sqft` (ranges like "1000-1200" replaced by averages)
  * Removed outliers based on **sqft per BHK ratio**
  * Simplified `location` by grouping less frequent values as **"other"**
  * Converted `availability` into binary (1 = Ready To Move, 0 = Others)

* **Encoding**:

  * One-hot encoding for categorical features (`area_type`, `location`)

---

## 🚀 Tech Stack

* **Python**
* **Flask**
* **Pandas & NumPy**
* **Scikit-learn**
* **Joblib**
* **HTML/CSS (Frontend)**

---

## 📌 Author

👤 Developed by Anuj Modani
