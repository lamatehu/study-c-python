import turtle
def main():
    turtle.hideturtle()
    turtle.setup(800,600)
    turtle.penup()
    turtle.pensize(2)
    turtle.goto(-300,-200)
    turtle.pencolor("green")
    turtle.pendown()
    leval = 3
    trunrun()
    turtle.done()
def trunrun():
    for i in range(12):
        koch(200,2)
        turtle.left(30)
def koch(size,j):
    if j == 0:
        turtle.fd(size)
    else:
        for angle in [0,60,-120,60]:
            turtle.left(angle)
            koch(size/3,j-1)
main()
