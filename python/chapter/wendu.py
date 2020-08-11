wendu = input()
if wendu[0] in ['F','f']:
    C = ((eval(wendu[1:]))-32)/1.8
    print("C{:.2f}".format(C))
elif wendu[0] in ['c','C']:
    F = (eval(wendu[1:]))*1.8+32
    print("F{:.2f}".format(F))
