count = 0
def hanoi(n,src,dst,mid):#圆盘的数量,原柱子，目标柱子，过度柱子
    global count#全局变量
    if n == 1:
      print("{}:{}->{}".format(1,src,dst))
      count = count+1
    else:
      hanoi(n-1,src,mid,dst)
      print("{}:{}->{}".format(n,src,dst))
      count = count + 1
      hanoi(n-1,mid,dst,src)
hanoi(3, 'a', 'c', 'b')
print(count)
