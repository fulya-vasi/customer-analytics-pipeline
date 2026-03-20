def analyze_results(df_model):
    print("\nCustomer Churn Analysis:")

    # Churn Rate
    churn_rate = df_model["prediction"].mean()
    print(f"\nChurn Rate: {churn_rate:.2%}")

    # Gruppenvergleich
    print("\nAverage values by predicted churn:")

    grouped = df_model.groupby("prediction")[[
        "income",
        "contracts",
        "website_visits",
        "support_tickets"
    ]].mean().round(2)

    print(grouped)

    # Top risky customers anzeigen
    high_risk = df_model[df_model["prediction"] == 1].head(5)

    print("\nExample High-Risk Customers:")
    print(high_risk)
