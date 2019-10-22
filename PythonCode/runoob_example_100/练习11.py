m = input('月:')
rabbit = [1,1]
for i in range(2,int(m)):# 从2到5
    rabbit.append(rabbit[i - 1 ]  +  rabbit[i - 2])
print(rabbit)
    
# 就是斐波那契
