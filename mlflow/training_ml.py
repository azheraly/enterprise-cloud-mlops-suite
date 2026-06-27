import mlflow
import pandas as pd
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
)
import matplotlib.pyplot as plt
import seaborn as sns
import pickle
# Set the tracking URI to a local database URI (e.g., sqlite:///mlflow.db).
# This is recommended option for quickstart and local development.
mlflow.set_tracking_uri("sqlite:///mlflow.db")
mlflow.set_experiment("first-experiment")


# Load the Iris dataset
X, y = datasets.load_iris(return_X_y=True)

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Define the model hyperparameters
params = {
    "solver": "lbfgs",
    "max_iter": 1000,
    "random_state": 8888,
}


# Step  - Log a model and metadata manually

# Start an MLflow run
with mlflow.start_run():
    # Log the hyperparameters
    mlflow.log_params(params)

    # Train the model
    lr = LogisticRegression(**params)
    lr.fit(X_train, y_train)

    # Log the model
    model_info = mlflow.sklearn.log_model(lr, name="Logistic_Regression_Model")
    
    with open("Logistic_Regression_Model.pkl", "wb") as f:
        pickle.dump(lr, f)
    mlflow.log_artifact("Logistic_Regression_Model.pkl")
        
    # Predict on the test set, compute and log the loss metric
    y_pred = lr.predict(X_test)
    # Metrics
    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred, average="weighted")
    recall = recall_score(y_test, y_pred, average="weighted")
    f1 = f1_score(y_test, y_pred, average="weighted")
    # Log metrics
    mlflow.log_metric("accuracy", accuracy)
    mlflow.log_metric("precision", precision)
    mlflow.log_metric("recall", recall)
    mlflow.log_metric("f1_score", f1)
    
    # Create confusion matrix

    # cm = confusion_matrix(y_test, y_pred)
    # plt.figure(figsize=(6,5))
    # sns.heatmap(
    #     cm,
    #     annot=True,
    #     fmt="d",
    #     cmap="Blues",
    #     xticklabels=lr.classes_,
    #     yticklabels=lr.classes_,
    # )

    # plt.xlabel("Predicted")
    # plt.ylabel("Actual")
    # plt.title("Confusion Matrix")

    # plt.savefig("confusion_matrix.png")
    # plt.show()
    # plt.close()

    # Upload to MLflow
    # mlflow.log_artifact("confusion_matrix.png")

    # Optional: Set a tag that we can use to remind ourselves what this run was for
    mlflow.set_tags({"name": "azher ali"})
    mlflow.log_artifact(__file__)



