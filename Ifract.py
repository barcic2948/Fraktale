import turtle

turtle.Screen()
turtle.tracer(1)
turtle.penup()
turtle.right(135)
turtle.fd(500)
turtle.left(135)
turtle.pendown()

turtle.speed(0)
def sier(side, level):
    if level == 1:
        for i in range(3):
            turtle.fd(side)
            turtle.left(120)
    else:
        sier(side/2, level-1)
        turtle.fd(side/2)
        sier(side/2, level-1)
        turtle.bk(side/2)
        turtle.left(60)
        turtle.fd(side/2)
        turtle.right(60)
        sier(side/2, level-1)
        turtle.left(60)
        turtle.bk(side/2)
        turtle.right(60)
def main():
    sier(800, 7)
    turtle.update()
    turtle.mainloop() 

if __name__ == '__main__':
    main()
    turtle.mainloop()

