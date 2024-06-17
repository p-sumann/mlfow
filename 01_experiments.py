import mlflow
import mlflow.experiments

if __name__ == "__main__":
    mlflow.create_experiment(
        name='suman_experiment',
        artifact_location='artifacts',
        tags={"env": "dev","version": "1.0"}
    )