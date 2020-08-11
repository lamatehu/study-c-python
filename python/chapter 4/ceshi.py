'''
m=10000
i = 0
while m > 1:
    print(i)
    m = m/2
print(i)

for i in range(1000,10000):
    m =str(i)
    f =pow(int(m[0]),4)+pow(int(m[1]),4)+pow(int(m[2]),4)+pow(int(m[3]),4)
    if f == i:
        print(f)
'''
num = []
i = 2
for i in range(2,100):
    j = 2
    for j in range(2,i):
        if(i%j==0):
            break
    else:
        print(i,end=' ')
    
