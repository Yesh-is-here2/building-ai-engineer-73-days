import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error

rng = np.random.default_rng(42)
X = rng.normal(size=(100,1))
y = 3*X[:,0] + 2 + rng.normal(scale=0.5, size=100)

df = pd.DataFrame({'x':X[:,0], 'y':y})
train_df, test_df = train_test_split(df, test_size=0.2, random_state=42)

m = LinearRegression()
m.fit(train_df[['x']], train_df['y'])
pred = m.predict(test_df[['x']])

mae = mean_absolute_error(test_df['y'], pred)
out = test_df.copy()
out['pred'] = pred
out.to_csv('predictions.csv', index=False)

print('MAE:', float(mae))
print('saved predictions.csv')
