from pathlib import Path
import os

def main():

    artifacts = Path("artifacts/files")
    artifacts.mkdir(parents=True, exist_ok=True)

    project = os.getenv("VERTEX_PROJECT", "")
    region = os.getenv("VERTEX_REGION", "us-central1")

    notes = f"""
Google Vertex AI Stub

This script is OFFLINE-SAFE.

If VERTEX_PROJECT is not set:
    → Only instructions are generated.

If VERTEX_PROJECT is set:
    → Shows commands for real usage.

Environment variables:

VERTEX_PROJECT = your GCP project id
VERTEX_REGION  = region (default us-central1)


Example:

PowerShell:

$env:VERTEX_PROJECT="my-project"
$env:VERTEX_REGION="us-central1"

python main.py


Example Vertex AI commands:

gcloud init

gcloud config set project <PROJECT_ID>

gcloud ai endpoints list --region {region}

"""

    (artifacts / "vertex_notes.txt").write_text(notes, encoding="utf-8")

    if not project:
        print("VERTEX_PROJECT not set. Offline stub mode.")
        print("Created artifacts/files/vertex_notes.txt")
        return

    print("Vertex AI configured")
    print("Project:", project)
    print("Region:", region)
    print("Created artifacts/files/vertex_notes.txt")


if __name__ == "__main__":
    main()