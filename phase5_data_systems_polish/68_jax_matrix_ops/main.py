import jax.numpy as jnp

A = jnp.array([[1.0, 2.0],[3.0, 4.0]])
B = jnp.array([[5.0, 6.0],[7.0, 8.0]])

C = A @ B
print(C)
