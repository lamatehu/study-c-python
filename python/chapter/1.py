'''
a = input("请输入一个⚪")
a = int(a)
b = 3.1415926
area = a * b * a
print(area)
print("{:.2f}".format(area))
'''
'''
#通心圆
import turtle
turtle.pensize(2)
turtle.circle(10)
turtle.circle(40)
turtle.circle(80)
turtle.circle(160)
'''

#五角星
from turtle import *
color("red","red")
begin_fill()
for i in range(5):
    fd(200)
    rt(144)
end_fill()
done()
