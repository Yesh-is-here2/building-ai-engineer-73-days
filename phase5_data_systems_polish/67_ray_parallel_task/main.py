import ray

ray.init(ignore_reinit_error=True)

@ray.remote
def square(x):
    return x * x

futures = [square.remote(i) for i in range(5)]
print(ray.get(futures))
