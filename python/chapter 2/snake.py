#pythondraw.py
import turtle
''''
t.setup(650,350,200,200)#设置绘图空间 #非必须
t.penup()
t.fd(-250)# 向前运行
t.pendown()
t.pensize(25)
t.pencolor('purple')
t.seth(-40) #通过角度来改变海龟的运行方向
for i in range(4):
    t.circle(40,80)
    t.circle(-40,80)
t.circle(40,80/2)
t.fd(40)
t.circle(16,180)
t.fd(40 * 2/3)
t .done()
#turtle.goto(x,y)

turtle.setup(600,600,0,0)
turtle.penup()
turtle.goto(-100,100)
turtle.pendown()
turtle.pensize(20)
turtle.pencolor("yellow")
turtle.seth(90)
turtle.fd(200)
turtle.seth(225)
turtle.goto(-100,-100)
turtle.seth(90)
turtle.fd(200)
turtle.colormod(255)
'''
'''
turtle.setup(800, 600,100, 100)

turtle.penup()

turtle.goto(-200, 100)

turtle.pendown()

turtle.pensize(5)

turtle.color('red', 'red')

turtle.begin_fill()

for i in range(2):

    turtle.fd(300)

    turtle.right(90)

    turtle.fd(200)

    turtle.right(90)

turtle.penup()

turtle.goto(-150, 70)

turtle.pendown()

for i in range(5):

    turtle.fd(40)

    turtle.right(144)

turtle.done()
'''
'''
turtle.setup(600,300)
turtle.penup()
turtle.goto(-100,100)
turtle.pendown()
turtle.pensize(4)
turtle.pencolor("black")
turtle.goto(100,100)
turtle.goto(100,-100)
turtle.goto(-100,-100)
turtle.goto(-100,100)
turtle.penup()
turtle.done()
'''
import turtle as t
t.pensize(2)
for i in range(8):
    t.fd(150)
    t.left(135)

turtle.done()
