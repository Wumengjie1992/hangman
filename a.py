#coding:utf-8
'''print("你好，早晨！")

name='小张'
print("你好，%-5s,小李"%name)

s="小妞|||王子"
result=s.split('|||')
print(result)
print("{0[0]},{0[1]}".format(result))



print('判断你好是否存在:%s'%("你好" in name) )

print("判断你好的位置:%d"%("你好，世界".index("世界")+1))
print("判断你好的位置:%d"%("你好，世界".find("世界")+1))

a=12
b=1.1
c='123'
d=1+2j

print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)
print(a**b)
print(a)
print(a%b)





import random

random_num1=random.randint(0,100)
random_num2=random.randrange(0,100)
print("随机数:%d,%d"%(random_num1,random_num2))
print("-"*60)


for i in range(0,10):			#for循环
    if i%2==0:
        print("偶数：%s"%i)
    else:
        print("奇数：%s"%i)

print('-'*60)
for i in range(0,10,3):			#for循环
    print(i)


print('-'*27,'九九乘法表','-'*27)
for i in range(1,10):
    for j in range(1,i+1):
        print("%s*%s=%2s"%(i,j,i*j),end='    ')
    print('\n')


print('-'*60)
count=0
for  x in 'ajdskjsahfksahfksfsffkjsfkjsfkjsf':
    if x is 'a':
        count+=1
print(count)

print('-'*60)
a=[chr(x) for x in range(ord('A'),ord('Z')+1)]
b=','.join(a)
print(b[0:10])
print(b[10:0:-1])
print(b[::-1])
print(b.reverse())
print(b)

d={'a':'A'}
print(d)

del d['a']
print(d)


with open(r'C:\Users\Administrator\Desktop\ab.txt',mode='w+',encoding='utf-8') as f:
    f.write('吴梦杰123')''''''
data = [(1,2,3),(4,5,8),(7,8,15),(4,1,5)]  
#元组前两个值，传入add函数的a和b参数
#第三个值期望值，用于断言的

#被测试对象：加法函数
def add(a,b):
    return a+b

test_cases = 0
success_test_cases = 0
fail_test_cases = 0 

#数据驱动模型：
for d in data:  #遍历所有的测试数据，每一次d变量取一个元组，例如：(1,2,3)
    test_cases+=1  #测试用例当前执行的总数
    result = add(d[0],d[1])  #d[0]表示元组中的第一个数据，d[1]是第二个数据
    print("result:",result)  #add函数调用的执行结果
    expected = d[2]          #元组中的第三个值，期望值
    print("expected:",d[2])  
    try:
        assert result==expected   #断言。如果表达式成立，就继续向下执行
                                  #不成立，抛出异常信息AssertionError
        success_test_cases+=1   #只有断言成功，才会增加成功用例计数
    except AssertionError as e:
        print("断言错误：实际值%s,期望值%s" %(result,expected))
        fail_test_cases+=1

print("测试用例一共执行了%s个" %test_cases)
print("测试用例一共成功执行了%s个" %success_test_cases)
print("测试用例一共失败执行了%s个" %fail_test_cases)


