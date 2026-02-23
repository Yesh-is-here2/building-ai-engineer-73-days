import os
from pathlib import Path

def main():
    artifacts_dir = Path("artifacts/files")
    artifacts_dir.mkdir(parents=True, exist_ok=True)

    host = os.getenv("EC2_HOST", "").strip()
    user = os.getenv("EC2_USER", "").strip() or "ubuntu"
    key  = os.getenv("EC2_KEY_PATH", "").strip()  # ex: C:\Users\akula\.ssh\mykey.pem
    port = os.getenv("EC2_PORT", "").strip() or "22"

    help_text = f"""AWS EC2 Connect (stub)

This script is OFFLINE-SAFE:
- If EC2_HOST is not set, it prints instructions and exits successfully.
- If EC2_HOST is set, it prints the SSH command you would run.

Environment variables:
  EC2_HOST      = public IPv4 / DNS of EC2 (required for real connect)
  EC2_USER      = login user (default: ubuntu)
  EC2_KEY_PATH  = path to your .pem private key (optional but usually needed)
  EC2_PORT      = SSH port (default: 22)

Example (PowerShell):
  $env:EC2_HOST="ec2-xx-xx-xx-xx.compute-1.amazonaws.com"
  $env:EC2_USER="ubuntu"
  $env:EC2_KEY_PATH="C:\Users\akula\.ssh\mykey.pem"
  python main.py

Notes:
- Windows OpenSSH needs private key permissions. If you get "Bad permissions", fix with:
  icacls "" /inheritance:r
  icacls "" /grant:r "akula:R"

Real SSH command template:
  ssh -i "<KEY_PATH>" -p {port} {user}@{host}

If using AWS SSM instead (no inbound SSH needed):
  aws ssm start-session --target <instance-id>
"""

    (artifacts_dir / "ssh_help.txt").write_text(help_text, encoding="utf-8")

    if not host:
        print("EC2_HOST is not set. Skipping real connection (offline-safe).")
        print("Wrote: artifacts/files/ssh_help.txt")
        return

    ssh_cmd = f'ssh -i "{key or "<PATH_TO_KEY.pem>"}" -p {port} {user}@{host}'
    print("EC2_HOST provided. This is the command you would run:")
    print(ssh_cmd)
    print("Wrote: artifacts/files/ssh_help.txt")

if __name__ == "__main__":
    main()
