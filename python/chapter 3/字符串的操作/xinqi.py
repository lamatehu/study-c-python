weekstr = '星期一星期二星期三星期四星期五星期六星期天'
m = eval(input("请输入一个数字"))
pos = (m-1)*3
print(weekstr[pos:pos+3])
