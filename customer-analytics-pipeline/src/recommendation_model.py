import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split


def train_recommendation_model(df):
    df_model = df.copy()

    df_model = pd.get_dummies(
        df_model,
        columns=["region", "customer_type"],
        drop_first=True
    )

    X = df_model.drop(["customer_id", "churn_risk"], axis=1)
    y = df_model["churn_risk"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = RandomForestClassifier(random_state=42)
    model.fit(X_train, y_train)

    df_model["prediction"] = model.predict(X)

    return model, df_model
