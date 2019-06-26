#coding:utf-8
import random

f=open('a.txt','r+')
k=1000
for num in range(1000):
    count=random.randint(5,10)
    f.write(','.join([str(i) for i in range(k,k+count)])+'\n')
    k+=count
f.close()

