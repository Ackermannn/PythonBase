# pickle  泡菜模块
'''
import pickle


# 泡菜
city = ['北京','上海','青岛']
pickle_file = open('city_data.pkl','wb')
pickle.dump(city,pickle_file)
pickle_file.close()



#读取
pickle_file = open('city_data.pkl','rb')
city2=pickle.load(pickle_file)
'''

## 莫烦示例 https://www.bilibili.com/video/av16926522/?p=34

import pickle

list1 = {'a':123,'b':45}

file = open('pickle_example.pickle','wb')
pickle.dump(list1,file)
file.close()


with open('pickle_example.pickle','rb') as file: #不怕忘掉 写 file.close()
    a_dict1=pickle.load(file)

    
print(a_dict1)

