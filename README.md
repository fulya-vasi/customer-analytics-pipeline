# Customer Churn Prediction Pipeline (Python)

## Context

This project simulates a customer analytics use case and demonstrates how machine learning can be used to identify customers with a high churn risk.

It is designed as an end-to-end pipeline that reflects real-world data workflows in a simplified and structured way.

## Overview

The pipeline generates synthetic customer data, stores it in a database, trains a machine learning model, predicts churn risk, and provides basic analysis and visualization of the results.

The goal is to demonstrate how business-relevant insights can be derived from data using a clean and modular approach.

## Use Case

Typical applications of this type of pipeline include:

- identifying customers with high churn risk  
- supporting retention strategies  
- prioritizing customer follow-ups  
- analyzing behavioral patterns  

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
5. Evaluate model performance (accuracy, classification report)  
6. Export predictions to CSV  
7. Save trained model  
8. Analyze customer segments  
9. Visualize churn distribution  
10. Visualize feature importance  
11. Predict churn risk for a new customer  

## Output

The pipeline generates the following outputs:

- `data/customer_data.db` (database)  
- `data/churn_predictions.csv` (predictions)  
- `data/churn_distribution.png` (visualization)  
- `data/feature_importance.png` (model insights)  
- `models/risk_model.pkl` (trained model)  

## Example Result

The model predicts whether a customer is likely to churn (`1`) or not (`0`) based on behavioral and demographic features.

Additional outputs include:

- churn rate  
- average values per risk group  
- feature importance ranking  

## Run the project

```bash
pip install -r requirements.txt
python main.py
