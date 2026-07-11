# 🏠 House Price Prediction System

A machine learning project that predicts residential property prices in Bengaluru based on features such as location, total area, number of bedrooms (BHK), and bathrooms.

**AIML Summer Internship 2026 — IIHMF, MNNIT Allahabad, Prayagraj**

---

## 📌 Problem Statement

Property pricing is often subjective and inconsistent, making it difficult for buyers, sellers, and agents to arrive at a fair value. This project builds a data-driven **regression model** that predicts a house's price from its measurable features, bringing objectivity to property valuation.

## 🎯 Objectives

- Clean and preprocess a messy, real-world housing dataset
- Perform exploratory data analysis (EDA) to uncover pricing patterns
- Engineer meaningful features (e.g., price per sqft, location grouping)
- Train and compare multiple regression models
- Deploy the best model as an interactive web application

## 📊 Dataset

- **Source:** Bengaluru House Price Data (Kaggle)
- **Size:** 13,320 records × 9 features
- **Target variable:** `price` (in lakhs ₹)
- **Key features:** `location`, `total_sqft`, `size` (BHK), `bath`, `balcony`

## 🛠️ Tech Stack

| Purpose | Tools |
|---|---|
| Language | Python 3.12 |
| Data handling | pandas, numpy |
| Visualization | matplotlib, seaborn |
| Modeling | scikit-learn, xgboost |
| Deployment | Streamlit |
| Environment | venv, Jupyter Notebook |

## 🧮 Machine Learning Workflow

1. **Data Cleaning** — handle missing values, fix the inconsistent `total_sqft` column, standardize the `size` column
2. **Feature Engineering** — create new features, reduce location categories, remove outliers
3. **EDA** — univariate, bivariate, and correlation analysis with visualizations
4. **Model Building** — Linear Regression, Random Forest, XGBoost
5. **Model Evaluation** — MAE, MSE, RMSE, R² Score
6. **Deployment** — Streamlit web app accepting user inputs and returning predictions

## 📁 Project Structure

HousePricePrediction/

├── Dataset/            # Raw dataset (CSV)

├── Notebook/           # Jupyter notebooks (EDA, modeling)

├── Model/              # Saved trained model

├── Streamlit_App/      # Deployment app

├── Documentation/      # Project report and presentation

├── .gitignore

└── README.md


## 🚀 How to Run

```bash
# Clone the repository
git clone https://github.com/DevK-26/HousePricePrediction.git
cd HousePricePrediction

# Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate

# Install dependencies
pip install numpy pandas matplotlib seaborn scikit-learn xgboost streamlit jupyter joblib

# Launch the Streamlit app (after Day 6)
streamlit run Streamlit_App/app.py
```

## 📈 Results

| Model | R² Score | RMSE |
|---|---|---|
| Linear Regression | 0.70 | 57.91 |
| Random Forest ✅ | 0.74 | 54.01 |
| XGBoost | 0.69 | 59.12 |

**Best model: Random Forest** (deployed in the Streamlit app)

## 👤 Author

Khushi Yadav

