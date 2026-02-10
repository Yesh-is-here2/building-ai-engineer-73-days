import time, random
for i in range(5):
    latency_ms = random.randint(50, 250)
    print("latency_ms=", latency_ms)
    time.sleep(0.2)
