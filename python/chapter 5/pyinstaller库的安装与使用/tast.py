import turtle
import time
def main(number):
    turtle.setup(800,400)
    turtle.penup()
    turtle.fd(-300)
    turtle.pensize(5)
    turtle.pencolor('red')
    drawdate(time.strftime('%Y-%m=%d+',time.gmtime()))
    #turtle.hideturtle()
    turtle.done()
def drawline(mod):
    print(mod)
    drawGap()
    if mod == 1:
        turtle.pendown()
        turtle.fd(50)
        turtle.penup()
        drawGap()
        turtle.right(90)
    else:
        turtle.fd(50)
        drawGap()
        turtle.right(90)
def drawGap():
    turtle.penup()
    turtle.fd(5)
def drawmod(number):
    if number in [2,3,4,5,6,8,9]:
        drawline(1)
    else:
        drawline(2)
    if number in [0,1,3,4,5,6,7,8,9]:
        drawline(1)
    else:
        drawline(2)
    if number in [0,2,3,5,6,8,9]:
        drawline(1)
    else:
        drawline(2)
    if number in [0,2,6,8]:
        drawline(1)
    else:
        drawline(2)
    turtle.left(90)
    if number in [0,4,5,6,8,9]:
        drawline(1)
    else:
        drawline(2)
    if number in [0,2,3,5,6,7,8,9]:
        drawline(1)
    else:
        drawline(2)
    if number in [0,1,2,3,4,5,6,7,8,9]:
        drawline(1)
    else:
        drawline(2)
    turtle.left(180)
    turtle.fd(50)
def drawdate(date):
    #date为日期，格式为"%y-%m=%d+"
    for i in date:
        if i == '-':
            turtle.write('年',font=('Arial',18,'normal'))
            turtle.fd(50)
            turtle.pencolor('grey')
        elif i == '=':
            turtle.write('月',font=('Asial',18,'normal'))
            turtle.fd(50)
            turtle.pencolor('blue')
        elif i == '+':
            turtle.write('日',font=('Asial',18,'normal'))
            turtle.fd(50)
        else:
            drawmod(eval(i))

main('1254')
