import pandas as pd
import matplotlib.pyplot as plt

def plot_feature_importance(model, feature_names):
    importance = pd.Series(model.feature_importances_, index=feature_names)
    importance = importance.sort_values()

    plt.figure(figsize=(10, 6))
    importance.plot(kind="barh", color="skyblue")

    plt.title("Customer Churn Drivers", fontsize=14)
    plt.xlabel("Importance Score")
    plt.ylabel("Features")

    plt.grid(axis="x", linestyle="--", alpha=0.7)

    plt.tight_layout()
    plt.savefig("data/feature_importance.png")
    plt.show()
