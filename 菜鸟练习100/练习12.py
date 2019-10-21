from math import sqrt

prime_count = 0
for i in range(101,201):
    maxj = int( sqrt( i ) )
    for j in range(2,maxj+1):
        if i % j == 0:
             break
        if j==maxj:
            print(i)
            prime_count += 1 
print('the totle is %d' % prime_count)
