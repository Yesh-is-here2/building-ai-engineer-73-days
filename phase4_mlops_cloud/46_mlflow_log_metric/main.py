import mlflow
mlflow.set_experiment("day46_demo")

with mlflow.start_run():
    mlflow.log_metric("accuracy", 0.9)
    print("logged metric to mlruns/")
