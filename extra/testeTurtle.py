import turtle
import colorsys 
sla= turtle.Turtle()
sla.speed(0)
s= turtle.Screen().bgcolor('black')
y= 0
n= 70
for i in range(360):
    c= colorsys.hsv_to_rgb(y, 1, 0.8)
    y+= 1/n
    sla.color(c)
    sla.lt(1)
    sla.fd(1)
    for j in range (2):
        sla.lt(2)
        sla.circle(50)
        for u in range(5):
            sla.lt(5)
            sla.circle(100)
turtle.mainloop()