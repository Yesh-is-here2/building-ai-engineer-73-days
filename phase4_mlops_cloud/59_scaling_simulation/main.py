import time
jobs = list(range(1, 11))
workers = 3

print("jobs:", jobs)
print("workers:", workers)

# simple simulation
for i, job in enumerate(jobs):
    w = (i % workers) + 1
    print(f"job {job} -> worker {w}")
    time.sleep(0.05)
