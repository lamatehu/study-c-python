
'''
time ctime gmtime
strftime strptime
sleeo p

time( 以浮点数来显示系统时间)
ctime() 字符串结果函数
gmtime() 不好认

时间格式化
strftime(tpl,ts)
%Y 年份 %m 月份 %B 月份名称
'''
import time
t = time.gmtime()
time.strftime("%Y-%m-%d %h:%M:%S",t)
