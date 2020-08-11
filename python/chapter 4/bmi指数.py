'''
mm = input("请输入你的体重（kg），你的身高（m）")
a = mm.split(',')
b = float(a[0])/pow(float(a[1]), 2)
print("{:.2f}".format(b))
if b >= 28:
    if b >= 30:
        print("不论国际国内都肥胖")
    else:
        print('国际不觉得胖')
elif 28>b>=24:
    if 30>b>=25:
        print('不论国际国内都偏胖')
    else:
        print('国际不觉得偏胖')
elif 25>b>=24:
    if 30>b>=25:
        print('不论国际国内都偏胖')
    else:
        print('国际不觉得偏胖')
'''
'''
height,weight = eval(input('请分别输入高和体重，中间以逗号隔开'))
bmi = weight/pow(height,2)
print('bmi的指数为{:.2f}'.format(bmi))
who,nat = '',''
if bmi < 18.5:
    who,nat ='偏瘦','偏瘦'
elif bmi < 24:
    who,nat ='正常','正常'
elif bmi < 25:
    who,nat ='正常','偏胖'
elif bmi <28:
    who,nat ='偏胖','偏胖'
elif bmi <30:
    who,nat ='偏胖','肥胖'
elif bmi >= 30:
    who,nat ='肥胖','肥胖'
else:
    print('输入错误')
'''
'''
m = 0
for i in range(966):
    if i%2 == 1:
        m=m+i
    else:
        m=m-i
print(m)
'''
'''
list =[]
for i in range(100,1000):
    m =str(i)
    if pow(int(m[0]),3)+pow(int(m[1]),3)+pow(int(m[2]),3) == i :
        list.append(i)
t = ''
for i in list:
    t = t +","+str(i)
print(t[1:])
'''
dict={'accout':'kate','password':'666666'}
i = 0
while i < 3:
    a = input()
    b = input()
    if a == str(dict['accout']):
        if b == str(dict['password']):
            print('登录成功!')
            break
        else:
            i=i+1
    else:
        i=i+1
else:
    print('3次用户名或者密码均有误！退出程序。')
