import numpy as np


class TabuTable:  # T表大小为3

    def __init__(self, size=3):
        self.size = size  # T表大小
        self.table = np.zeros((self.size, 2))  # 禁忌表初始化

    def put(self, position):
        for i in range(self.size - 1, 1, -1):
            self.table[i, :] = self.table[i-1, :]
        self.table[0, :] = position[1:]

    def check(self, position):
        for i in range(self.size):
            if np.array(self.table[i, :] == position[1:]).all():
                return True
        return False


def total_distance(s, D):
    out_sum = 0
    for i in range(s.size):
        if i < s.size - 1:
            out_sum += D[s[i][0], s[i + 1][0]]
        else:
            out_sum += D[s[i][0], s[0][0]]
    return out_sum


def nerbor(s, D):
    res = []
    for i in range(1, s.size - 1):
        for j in range(i + 1, s.size):
            temp_s = s.copy()
            temp = temp_s[i].copy()
            temp_s[i] = temp_s[i+1].copy()
            temp_s[i+1] = temp.copy()
            res.append([total_distance(temp_s,D),i,j])
    res = np.array(res)
    res = res[np.argsort(res[:, 0]), :]  # 对总路径值排序
    return res


D = np.array([[0, 10, 15,  6,  2],
             [10,  0,  8, 13,  9],
             [15,  8,  0, 20, 15],
              [6, 13, 20,  0,  5],
              [2,  9, 15,  5,  0]])
s = np.arange(5).reshape(5, 1)
t = TabuTable()
minD = total_distance(s, D)
historyMin = minD.copy()
print(minD)
for _ in range(5):
    res = nerbor(s, D)
    each = res[0, :]  # 这里选取的是最小的 修改 ->选取不被禁忌的
    for i in range(t.size):
        if (not t.check(each)) or (each[0] <= historyMin):  # or破禁
            t.put(each)
            break
        else:
            each = res[i + 1, :]
    t.put(each)
    temp = s[each[1]].copy()  # swap
    s[each[1]] = s[each[2]]
    s[each[2]] = temp.copy()
    print(s)
    minD = total_distance(s, D)
    if minD < historyMin:
        historyMin = minD.copy()
    print(minD)



