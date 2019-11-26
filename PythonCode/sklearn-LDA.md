# introduce

使用LDA算法对sklearn人脸数据集合进行降维,再使用后KNN算法进行分类.

# reference

https://www.cnblogs.com/pinard/p/6249328.html
https://blog.csdn.net/zhangliaobet/article/details/78315879

# code
```python
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 22:28:31 2019

@author: Administrator
"""
import numpy as np
from sklearn.datasets import fetch_lfw_people
from sklearn.model_selection import train_test_split
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.neighbors import KNeighborsClassifier
people = fetch_lfw_people(min_faces_per_person=20,resize=0.7) # 读取数据集 

# 对数据偏斜进行处理
mask = np.zeros(people.target.shape, dtype=np.bool) 
for target in np.unique(people.target):     
    mask[np.where(people.target == target)[0][:50]] = 1 
X_people = people.data[mask]
y_people = people.target[mask]

# 数据训练测试集 分割
X_train, X_test, y_train, y_test = train_test_split(X_people, y_people, 
                                            stratify=y_people, random_state=0) 
lda = LinearDiscriminantAnalysis(n_components=50)
lda.fit(X_train,y_train) # lda模型训练
X_train_lda = lda.transform(X_train) # 转换 
X_test_lda = lda.transform(X_test) # 转换
print("X_train_lda.shape: {}".format(X_train_lda.shape))

# 使用k临近分类器
knn = KNeighborsClassifier(n_neighbors=1)  
knn.fit(X_train_lda, y_train) 
print("使用LDA降维, Test set accuracy: {:.2f}".format(knn.score(X_test_lda, y_test)))
# 使用k临近分类器
knn = KNeighborsClassifier(n_neighbors=1)  
knn.fit(X_train, y_train) 
print("不使用LDA降维 :Test set accuracy: {:.2f}".format(knn.score(X_test, y_test)))
```
