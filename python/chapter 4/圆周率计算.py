'''
'圆周率法'
a = 100
b = 0
for i in range(a):
    b = b+(1/pow(16,i))*(4/(8*i+1)-2/(8*i+4)-1/(8*i+5)-1/(8*i+6))

print("圆周率为{:.6f}".format(b))
'''''''''
'''''
from random import random
from time import perf_counter
DARTS = 1000*1000
hits = 0.0
start =perf_counter()
for i in range(1,DARTS+1):
    x,y = random(),random()
    dist = pow(x ** 2 + y ** 2,0.5)
    if dist <= 1.0:
        hits = hits + 1
pi = 4 * (hits/DARTS)
print("圆周率的值是{}".format(pi))
print("运行时间是:{:5f}s".format(start))
'''
height,weight = eval(input('请输入你的身高体重,让我来计算你的bmi,中间用,隔开'))
bmi = weight / pow(height,2)
if bmi < 18.5:
    c,d = '偏廋','偏瘦'
elif 18.5 < bmi < 24:
    c,d ='正常','正常'
elif 24 < bmi < 25:
    c,d ='偏胖','正常'
elif 25 < bmi < 28:
    c,d ='偏胖','偏胖'
elif 28 <= bmi < 30:
    c,d = '肥胖','偏胖'
elif 30<= bmi:
    c,d = '肥胖','肥胖'
else:
    print('你输入的信息不准确')
print("bmi数值为:{:.2f}".format(bmi))
print("BMI指标为:国际'"+d+"',国内'"+c+"'")
{}
