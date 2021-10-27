import turtle  

global mult
mult = 1.3

wn = turtle.Screen()
wn.tracer(0) 

tur = turtle.Turtle()
tur.right(90)
tur.penup()
tur.forward(300)
tur.right(180)
tur.speed(0)
tur.forward(300)
tur.pendown()

def draw(x, y, a):
    wn.update()
    if(x<y):
        return 0
    else:
        tur.left(a)
        tur.forward(x)
        draw(x/mult,y,a)
        tur.back(x)
        tur.right(2*a)
        tur.forward(x)
        draw(x/mult,y,a)
        tur.back(x)
        tur.left(a)
tab = ["red","green","blue","black"]
for i in range(3):
    tur.color(tab[i])
    draw(100, 10, 60)
    tur.right(90)

wn.update()
wn.mainloop() 

