'''
import time
time.ctime()
name = '1234567'
print(name[-1],name[1],name[2:-2])
print("{0:3}".format(name))

a = input()
b = pow(int(a),0.5)
c=("{:.3f}".format(b))
e =(30-len(c)) * '+'
print("{:<}{}".format(e,c))

s = 'hah-fufu-mm-dd'
p = s.split('-')
print(p[0]+'+'+p[-1])


a =  1
for i in range(365):
    a= a*1.01
m = ("{:.2f}".format(a))
float(m)


def Mb(df):
    b = 1
    for i in range(365):
        if i % 7 in [0,6]:
            b = b * 0.99
        else:
            b = b * (1 + df)
    return b
dy = 0.01
while Mb(dy) < 37.78:
    dy = dy + 0.001
print('工作日的努力参数是: {:.3f}'.format(dy))
'''
import time
def dv(x):
    a = pow(x,3)
    m = len(str(a))
    e = (20-m)/2
    time.sleep(1)
    f = int(e) * '-'
    print("\r"+f+'{:^}'.format(a)+f,end='')
    return
for i in range(30):
    dv(i)
