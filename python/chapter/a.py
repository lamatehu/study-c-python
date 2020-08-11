'''
template = "零一二三四五六七八九"
s = input()
for c in s:
    print(template[eval(c)],end="")
'''
'''
A = input()
M = A[0:-3]
print(M)
if M in ('RMB','rmb'):
    print("OK")
'''
'''
a = input()
if eval(a) == 0:
    print("Hello World")
elif eval(a) < 0:
    m = "Hello World"
    for b in m:
        print(b)
elif eval(a) > 0:
    m = "Hello World"
    for b in m:
'''
a = input()
b = eval(a)
print("{:.2f}".format(b))
