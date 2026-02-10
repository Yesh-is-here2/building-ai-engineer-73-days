import numpy as np
from sklearn.linear_model import LinearRegression

X = np.array([[1],[2],[3],[4]], dtype=float)
y = np.array([2,4,6,8], dtype=float)

m = LinearRegression()
m.fit(X, y)

print('coef:', float(m.coef_[0]))
print('intercept:', float(m.intercept_))
print('predict(5):', float(m.predict([[5]])[0]))
