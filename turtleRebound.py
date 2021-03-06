import turtle

def askForAngle():
    angle = int(input("Enter the starting angle (0 to 360) => "))
    if angle > 360 or angle < 0:  #if bad angle
        askForAngle()
    else:
        return angle

def askForSpeed():
    speed = int(input("Enter the speed (1 fast to 10 slow) => "))
    if speed > 10 or speed < 1:  #if bad speed
        askForSpeed()
    else:
        return speed
                  
angle = askForAngle()
speed = askForSpeed()

wn = turtle.Screen()
t = turtle.Turtle()
windowHeight = turtle.window_height()-40

wn.tracer(False)
t.up()
t.forward(windowHeight/2)
t.left(90)
t.forward(windowHeight/2)
t.left(90)
t.down()
for i in range(4):
    t.forward(windowHeight)
    t.left(90)
t.up()
t.right(180)
t.goto(0,0)
wn.tracer(True)

t.color("green")
t.speed(speed)

#print(t.speed())

wn.tracer(False)
t.left(angle)
wn.tracer(True)

while True:
    t.forward(4)
    x,y = t.position()
    currentAngle = t.heading()
    #print(abs(x),abs(y),currentAngle)
    if abs(x) >= windowHeight/2 and abs(y) >= windowHeight/2:
        wn.tracer(False)
        t.left(180)
        wn.tracer(True)
        t.forward(6)
    elif abs(x) >= windowHeight/2:
        if currentAngle == 0 or currentAngle == 90 or currentAngle == 180 or currentAngle == 270 or currentAngle == 360:
            wn.tracer(False)
            t.right(180)
            wn.tracer(True)
            t.forward(6)
        elif currentAngle < 90 or (currentAngle > 180 and currentAngle < 270):
            wn.tracer(False)
            t.left(180-(currentAngle*2))  #works
            wn.tracer(True)
            t.forward(6)
        elif (currentAngle > 90 and currentAngle < 180) or currentAngle > 270:
            wn.tracer(False)
            t.right((currentAngle-90)*2)  #works
            wn.tracer(True)
            t.forward(6)
            
    elif abs(y) >= windowHeight/2:
        if currentAngle == 0 or currentAngle == 90 or currentAngle == 180 or currentAngle == 270 or currentAngle == 360:
            wn.tracer(False)
            t.right(180)
            wn.tracer(True)
            t.forward(6)
        elif currentAngle < 90 or (currentAngle > 180 and currentAngle < 270):
            wn.tracer(False)
            t.right((currentAngle-180)*2)  #works
            wn.tracer(True)
            t.forward(6)
        elif (currentAngle > 90 and currentAngle < 180) or currentAngle > 270:
            wn.tracer(False)
            t.left((180-currentAngle)*2)  #works
            wn.tracer(True)
            t.forward(6)
        
            
        


    
