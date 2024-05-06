from dotenv import load_dotenv
from constants import *
import subprocess

# Define the MLflow server command
mlflow_command = [
    "mlflow", "server",
    "--host", HOST,
    "--port", PORT,
    "--artifacts-destination", ARTIFACTS_DESTINATION,
    "--backend-store-uri", BACKEND_STORE_URI,
    "--default-artifact-root", DEFAULT_ARTIFACT_ROOT
]

# Execute the MLflow server command
subprocess.Popen(mlflow_command)

if __name__ == '__main__':
    load_dotenv()
    # Execute the MLflow server command
    subprocess.Popen(mlflow_command)