def print_churn_summary(df):
    print("\nChurn Risk Summary:")
    print(df["prediction"].value_counts())

    print("\nAverage values by predicted churn risk:")
    print(
        df.groupby("prediction")[["income", "contracts", "website_visits", "support_tickets"]]
        .mean()
        .round(2)
    )

