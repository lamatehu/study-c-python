# 请在...补充一行或多行代码

def fbi(n):
    m= 0
    if n <= 2:
        m = 1
    else:
        m = fbi(n-1)+fbi(n-2)
    return m

n = eval(input())
print(fbi(n))
