from src.analysis import analyze_results
from src.generate_data import generate_customer_data
from src.recommendation_model import train_recommendation_model
from src.storage import save_to_sqlite
from src.evaluate import print_churn_summary
from src.export import export_predictions
from src.visualize import plot_churn_distribution


def main():
    print("Erzeuge Kundendaten...")
    df = generate_customer_data()

    print(df.head())

    print("Trainiere Modell...")
    model, df_model = train_recommendation_model(df)

    print_churn_summary(df_model)
    export_predictions(df_model)
    plot_churn_distribution(df_model)

    print(df_model[["customer_id", "age", "income", "contracts", "website_visits", "support_tickets", "churn_risk", "prediction"]].head())
    analyze_results(df_model)
    print("Speichere Daten in SQLite...")
    save_to_sqlite(df_model)

    print("Fertig! Pipeline abgeschlossen.")


if __name__ == "__main__":
    main()
