import pandas as pd
import numpy as np
from sklearn.ensemble import IsolationForest
import matplotlib.pyplot as plt

def generate_data(n=200):
    np.random.seed(42)

    temperature = np.random.normal(50, 5, n)
    pressure = np.random.normal(100, 10, n)

    df = pd.DataFrame({
        "temperature": temperature,
        "pressure": pressure
    })

    anomalies = pd.DataFrame({
        "temperature": [80, 85, 90],
        "pressure": [150, 160, 170]
    })

    df = pd.concat([df, anomalies], ignore_index=True)

    return df


def detect_anomalies(df):
    model = IsolationForest(contamination=0.05, random_state=42)
    df["anomaly"] = model.fit_predict(df)

    return df


def main():
    print("Erzeuge Daten...")
    df = generate_data()

    print("Erkenne Anomalien...")
    df = detect_anomalies(df)

    print(df.tail(10))

    plt.scatter(df["temperature"], df["pressure"], c=df["anomaly"])
    plt.xlabel("Temperature")
    plt.ylabel("Pressure")
    plt.title("Anomaly Detection")
    plt.show()

    df.to_csv("data/output.csv", index=False)
    print("Gespeichert in data/output.csv")


if __name__ == "__main__":
    main()


