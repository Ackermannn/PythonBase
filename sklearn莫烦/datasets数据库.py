from __future__ import print_function
from sklearn import datasets
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

loaded_data = datasets.load_boston()
data_X = loaded_data.data
data_y = loaded_data.target  # target 是 标签

model = LinearRegression()  # 入门级用默认参数 了解的话 可以修改值
model.fit(data_X, data_y)

print(model.predict(data_X[:4, :]))
print(data_y[:4])


# 自己创造数据
X, y = datasets.make_regression(n_samples=100, n_features=1, n_targets=1, noise=20)
plt.scatter(X, y)
plt.show()


