# 请在...补充一行或多行代码
def cmul(a,*b):
    m = a
    for i in b:
        m = i * m
    return m




print(eval("cmul({})".format(input())))
