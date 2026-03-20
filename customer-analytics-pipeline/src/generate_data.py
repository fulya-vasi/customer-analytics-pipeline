import pandas as pd
import numpy as np

def generate_customer_data(n=500, seed=42):
    np.random.seed(seed)

    customer_id = np.arange(1, n + 1)
    age = np.random.randint(18, 75, n)
    income = np.random.randint(20000, 120000, n)
    contracts = np.random.randint(1, 6, n)
    website_visits = np.random.randint(1, 50, n)
    support_tickets = np.random.poisson(1.5, n)
    region = np.random.choice(["north", "south", "east", "west"], n)
    customer_type = np.random.choice(["new", "standard", "premium"], n, p=[0.3, 0.5, 0.2])

    df = pd.DataFrame({
        "customer_id": customer_id,
        "age": age,
        "income": income,
        "contracts": contracts,
        "website_visits": website_visits,
        "support_tickets": support_tickets,
        "region": region,
        "customer_type": customer_type
    })

    churn_score = (
        (df["contracts"] == 1).astype(int)
        + (df["website_visits"] < 5).astype(int)
        + (df["support_tickets"] >= 3).astype(int)
        + (df["customer_type"] == "new").astype(int)
    )

    df["churn_risk"] = (churn_score >= 2).astype(int)

    return df
