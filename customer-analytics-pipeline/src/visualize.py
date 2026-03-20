import matplotlib.pyplot as plt

def plot_churn_distribution(df):
    counts = df["prediction"].value_counts()

    plt.figure(figsize=(8, 5))
    counts.plot(kind="bar")
    plt.title("Predicted Churn Risk Distribution")
    plt.xlabel("Prediction (0 = Low Risk, 1 = High Risk)")
    plt.ylabel("Number of Customers")
    plt.tight_layout()
    plt.savefig("data/churn_distribution.png")
    plt.show()
