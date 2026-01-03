import matplotlib.pyplot as plt

models = ["Linear", "LSTM + Attention", "XGBoost"]
maes = [0.06494, 0.05838, 0.03505]  # Read from Kaggle submission results
plt.bar(models, maes, color=["blue", "orange", "green"])
plt.ylabel("Mean Absolute Error (MAE)", fontsize=14)
plt.title("Model Performance Summary", fontsize=18)
plt.tick_params(axis='x', labelsize=13)
plt.tight_layout()
for i, (model, mae) in enumerate(zip(models, maes)):
    plt.text(i, mae, f"{mae:.3f}", ha='center', va='bottom', fontsize=12)
plt.savefig("doc/model_performance_summary.png")
