#关于7段式数码管
import turtle
import time
def main():
    turtle.setup(800 , 600)
    turtle.pencolor('red')
    turtle.pensize('5')
    turtle.penup()
    turtle.goto(-200, 200)
    shulie()
    turtle.hideturtle()
    turtle.done()
def shulie():
    tmi = time.strftime("%Yy%mm%dds%HD%M", time.localtime())
    for i in tmi:
        turtle.fd(50)
        if i == 'y':
            turtle.fd(50)
            turtle.pendown()
            turtle.write('年', font=('Arial', 18, 'normal'))
            turtle.penup()
        elif i == 'm':
            turtle.write('月',font=('Arial',18,'normal'))
            turtle.up()
        elif i == 'd':
            turtle.write('日',font=('Arial',18,'normal'))
            turtle.penup()
        elif i == 's':
            turtle.goto(-200,-50)
            turtle.penup()
        elif i == 'D':
            turtle.write(':', font=('Arial', 18, 'normal'))
            turtle.penup()
        else: #in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
            sevenmod(i)
def ledpipe(mod):
    print(mod)
    if mod == 1:
        turtle.pencolor("green")
        turtle.pensize(10)
        turtle.pendown()
        turtle.fd(50)
        turtle.right(90)
        turtle.penup()
    else:
        turtle.penup()
        turtle.fd(50)
        turtle.right(90)
def sevenmod(number):
    number = int(number)
    if number in [2,3,4,5,6,8,9]:#1
        ledpipe(1)
    else:
        ledpipe(0)
    if number in [0,1,3,4,5,6,7,8,9]:#2
        ledpipe(1)
    else:
        ledpipe(0)
    if number in [0,2,3,5,6,8,9]:#3
        ledpipe(1)
    else:
        ledpipe(0)
    if number in [0,2,6,8]:#4
        ledpipe(1)
    else:
        ledpipe(0)
    turtle.left(90)
    if number in [0,4,5,6,7,8,9]:#5
        ledpipe(1)
    else:
        ledpipe(0)
    if number in [0, 2, 3, 5, 6, 7, 8, 9]:#6
        ledpipe(1)
    else:
        ledpipe(0)
    if number in [0, 1, 2, 3, 4, 7, 8, 9]:#7
        ledpipe(1)
    else:
        ledpipe(0)
    turtle.left(180)
#main()
main()
print(time.strftime("%Y-%m-%d %H:%M",time.localtime()))
print(time.strftime("%Yy%mm%dds%HD%M", time.localtime()))
