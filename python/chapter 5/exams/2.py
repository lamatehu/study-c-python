
import turtle
def koch(size, n):
    if n == 0:
        turtle.fd(size)
    else:
        for anger in [0, 60, -120, 60]:
            turtle.right(anger)
            koch(size/3, n-1)


def main(level):
    a= level
    turtle.setup(600, 600)
    turtle.penup()
    turtle.goto(-200, 100)
    turtle.pendown()
    turtle.pensize(2)
    koch(200, a)
    turtle.done()

try:
    level = eval(input("请输入科赫曲线的阶: "))
    main(level)
except:
    print("输入错误")
