import numpy as np

def totalDistance(s,D):
    sumD = 0
    for i in range(s.size):
        if i < s.size - 1:
            sumD += D[s[i][0],s[i+1][0]]
        else:
            sumD += D[s[i][0],s[  0][0]]
    return sumD

def nerbor(s,D):
    res = []
    for i in range(1,s.size-1 ):
        for j in range(i + 1, s.size):
            temp_s = s.copy()
            temp = temp_s[i].copy()
            temp_s[i] = temp_s[i+1].copy()
            temp_s[i+1] = temp.copy()
            res.append([totalDistance(temp_s,D),i,j])
    res = np.array(res)
    return res


D = np.array([[0,10,15, 6, 2],
             [10, 0, 8,13, 9],
             [15, 8, 0,20,15],
             [ 6,13,20, 0, 5],
             [ 2, 9,15, 5, 0]])



s = np.arange(5).reshape(5,1)

minD = totalDistance(s,D)
res = nerbor(s,D)

#np.random.shuffle(s[1:])
print(s)

for i in range(5):
    print('这是第',i,'次循环')
    res = nerbor(s,D)
    each = res[res[:,0].argmin(),:]
    if each[0] <= minD:
        minD = each[0]
        temp = s[each[1]].copy()
        s[each[1]] = s[each[2]].copy()
        s[each[2]] = temp.copy()
        minD = totalDistance(s,D)
        print(s)
        print(minD)
        


