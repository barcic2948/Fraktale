import turtle
screen = turtle.Screen()
screen.title('Triangle Spiral')
turtle.setup(500,500)
screen.setworldcoordinates(-1000,-1000,1000,1000)
turtle.speed(0)
turtle.hideturtle()

for i in range(5,10000,6):
    turtle.fd(i)
    turtle.left(119.3)