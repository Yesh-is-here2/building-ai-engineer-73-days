import os
from pathlib import Path

def main():
    artifacts_dir = Path("artifacts/files")
    artifacts_dir.mkdir(parents=True, exist_ok=True)

    info_text = """AWS SageMaker Notebook Demo (stub)

This script is OFFLINE-SAFE.

It demonstrates how SageMaker notebooks are typically used
in ML engineering workflows.

Typical workflow:

1. Create SageMaker notebook instance
2. Upload dataset
3. Train model
4. Save model artifacts to S3
5. Deploy endpoint

Example AWS CLI commands:

Create notebook:

aws sagemaker create-notebook-instance \
  --notebook-instance-name ml-notebook \
  --instance-type ml.t2.medium \
  --role-arn <role-arn>

Stop notebook:

aws sagemaker stop-notebook-instance \
  --notebook-instance-name ml-notebook

Delete notebook:

aws sagemaker delete-notebook-instance \
  --notebook-instance-name ml-notebook

In real ML systems SageMaker notebooks are used for:

- Data exploration
- Model training
- Experiments
- Prototyping
"""

    (artifacts_dir / "sagemaker_notes.txt").write_text(info_text)

    print("SageMaker notebook demo stub executed.")
    print("Created file: artifacts/files/sagemaker_notes.txt")
    print("In a real system this would run inside SageMaker.")


if __name__ == "__main__":
    main()