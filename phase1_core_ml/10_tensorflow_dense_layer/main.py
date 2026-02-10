import numpy as np
import tensorflow as tf

model = tf.keras.Sequential([tf.keras.layers.Dense(1, input_shape=(1,))])
model.compile(optimizer='sgd', loss='mse')

X = np.array([[1],[2],[3],[4]], dtype=float)
y = np.array([[2],[4],[6],[8]], dtype=float)

model.fit(X, y, epochs=30, verbose=0)
pred = model.predict(np.array([[5.0]]), verbose=0)[0][0]
print('pred(5):', float(pred))
