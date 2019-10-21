from __future__ import print_function
from sklearn import datasets
from sklearn.linear_model import LinearRegression

loaded_data = datasets.load_boston()
data_X = loaded_data.data
data_y = loaded_data.target

model = LinearRegression()
model.fit(data_X, data_y)

print(model.predict(data_X[:4, :]))
print(model.coef_)  # 比如 y = 0.1x+ 0.3
print(model.intercept_)
print(model.get_params())  # 拿出model里的参数
print(model.score(data_X, data_y))  # R^2 coefficient of determination # 打分


