# Customer Churn Prediction Pipeline (Python)

## Context

This project simulates a customer analytics use case and demonstrates how machine learning can be used to identify customers with a high churn risk.

It is designed as a simple end-to-end analytics and prediction pipeline with a business-oriented focus.

## Overview

The project generates synthetic customer data, stores it in SQLite, trains a machine learning model, predicts churn risk, and provides basic business insights through summary analysis and visualizations.

It combines elements of:

- data generation
- data storage
- machine learning
- prediction
- business analysis
- visualization

## Use Case

The project is inspired by common analytics use cases such as:

- identifying customers with high churn risk
- supporting retention strategies
- prioritizing follow-up actions for at-risk customers
- improving customer analytics with interpretable model outputs

## Technologies

- Python
- pandas
- numpy
- scikit-learn
- SQLite
- matplotlib
- joblib

## Pipeline Steps

1. Generate synthetic customer data
2. Store structured data in SQLite
3. Train a Random Forest classification model
4. Predict churn risk
5. Export predictions to CSV
6. Save the trained model
7. Analyze customer groups by predicted churn risk
8. Visualize churn distribution
9. Visualize feature importance
10. Predict churn risk for a new customer example

## Project Structure

```text
customer-analytics-pipeline/
├── data/
│   ├── customer_data.db
│   ├── churn_predictions.csv
│   ├── churn_distribution.png
│   └── feature_importance.png
├── models/
│   └── risk_model.pkl
├── src/
│   ├── generate_data.py
│   ├── storage.py
│   ├── recommendation_model.py
│   ├── evaluate.py
│   ├── export.py
│   ├── visualize.py
│   ├── feature_importance.py
│   ├── save_model.py
│   ├── predict.py
│   ├── analysis.py
│   └── metrics.py
├── main.py
├── requirements.txt
└── README.md
