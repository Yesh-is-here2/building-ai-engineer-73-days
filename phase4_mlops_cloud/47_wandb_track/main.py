import wandb
import random
import time

wandb.init(
    project="phase4_47_wandb_tracking",
    config={
        "learning_rate": 0.01,
        "batch_size": 32,
        "optimizer": "adam"
    }
)

for epoch in range(5):
    loss = random.uniform(0.1, 1.0)
    accuracy = random.uniform(0.7, 0.99)

    wandb.log({
        "epoch": epoch,
        "loss": loss,
        "accuracy": accuracy
    })

    print(f"Epoch {epoch}: loss={loss:.4f}, accuracy={accuracy:.4f}")
    time.sleep(0.5)

wandb.finish()
print("Run complete.")
