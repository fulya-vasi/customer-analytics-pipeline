def export_predictions(df, output_path="data/churn_predictions.csv"):
    df.to_csv(output_path, index=False)
