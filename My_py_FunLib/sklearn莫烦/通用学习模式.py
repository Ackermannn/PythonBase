# link:
# https://www.bilibili.com/video/av17003173/
import numpy as np
from sklearn import datasets  # 有很多数据库
from sklearn.model_selection import train_test_split
    # from sklearn.cross_validation import train_test_split已经弃用
from sklearn.neighbors import KNeighborsClassifier

iris = datasets.load_iris()
iris_X = iris.data
iris_y = iris.target

# print(iris_X[:2, :])
# print(iris_y)

# 数据分开
X_train, X_test, y_train, y_test = train_test_split(iris_X, iris_y, test_size=0.3)

# print(y_train)  # 正好打乱了

knn = KNeighborsClassifier()
knn.fit(X_train, y_train)  # 所有train 的步骤都在这里

print(knn.predict(X_test))
print(y_test)
c = list(knn.predict(X_test) == y_test)
print('True number:', c.count(True))
print('False number:', c.count(False))
print('accuracy: %.3f' % (c.count(True) / (c.count(True) + c.count(False))) )



