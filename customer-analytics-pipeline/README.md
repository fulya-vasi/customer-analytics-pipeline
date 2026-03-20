# Customer Churn Prediction Pipeline (Python)

## Context

This project simulates a real-world customer analytics use case: predicting customer churn risk.

It demonstrates how machine learning can be used to identify customers who are likely to leave a service, enabling proactive retention strategies.

---

## Overview

This project builds an end-to-end machine learning pipeline:

- Data generation (customer behavior simulation)
- Feature engineering
- Model training (Random Forest)
- Churn prediction
- Data analysis
- Visualization
- Export to database and CSV

---

## Data Pipeline

<img src="images/pipeline-diagram.png" width="300">

---

## Technologies

- Python
- pandas
- numpy
- scikit-learn
- matplotlib
- SQLite
- joblib

---

## What it does

- Generates synthetic customer data
- Calculates churn risk based on behavior patterns
- Trains a machine learning model
- Predicts churn probability
- Analyzes high-risk customers
- Saves results to database and CSV
- Visualizes churn distribution and feature importance

---

## Output

- `data/customer_data.db` → SQLite database  
- `data/churn_predictions.csv` → predictions  
- `data/churn_distribution.png` → churn visualization  
- `data/feature_importance.png` → model insights  

---

## Example Insights

- Churn Rate calculation
- Average values by churn group
- Identification of high-risk customers

---

## Run the project

```bash
pip install -r requirements.txt
python main.py
