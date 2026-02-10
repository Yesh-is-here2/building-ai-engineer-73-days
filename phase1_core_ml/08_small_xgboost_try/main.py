import numpy as np
import xgboost as xgb

X = np.array([[1],[2],[3],[4],[5]], dtype=float)
y = np.array([0,0,0,1,1], dtype=float)

d = xgb.DMatrix(X, label=y)
params = {'objective':'binary:logistic','max_depth':2,'eta':0.3,'eval_metric':'logloss'}
bst = xgb.train(params, d, num_boost_round=10)

p = bst.predict(xgb.DMatrix(np.array([[2.5]], dtype=float)))[0]
print('pred prob for 2.5:', float(p))
