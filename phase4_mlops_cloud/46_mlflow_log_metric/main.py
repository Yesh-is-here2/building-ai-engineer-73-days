import mlflow
import random
import time

mlflow.set_tracking_uri("sqlite:///mlflow.db")
mlflow.set_experiment("phase4_46_mlflow_experiment")

with mlflow.start_run():

    mlflow.log_param("learning_rate", 0.01)
    mlflow.log_param("batch_size", 32)
    mlflow.log_param("optimizer", "adam")

    for epoch in range(5):
        loss = random.uniform(0.1, 1.0)
        accuracy = random.uniform(0.7, 0.99)

        mlflow.log_metric("loss", loss, step=epoch)
        mlflow.log_metric("accuracy", accuracy, step=epoch)

        print(f"Epoch {epoch}: loss={loss:.4f}, accuracy={accuracy:.4f}")
        time.sleep(0.5)

print("Run complete.")
