import turtle
import math
import random

wn = turtle.Screen()
fred = turtle.Turtle()
fred.speed(0)
wn.tracer(100)

wn = turtle.Screen()
wn.setworldcoordinates(-1000,-1000,1000,1000)

fred.up()

numdarts = 1000
insideCount = 0
for i in range(numdarts):
    randx = random.randrange(-1000, 1001)
    randy = random.randrange(-1000, 1001)
    fred.goto(randx,randy)
    if fred.distance(0,0) <= 1000:
        insideCount += 1
        fred.color("red")
    else:
        fred.color("blue")
    fred.stamp()

print("Pi is approxiametly",(insideCount/numdarts)*4,"units.")
wn.exitonclick()
