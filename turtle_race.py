import turtle as t
import random, sys
random_forward=random.randint(1,20)

turtle1=t.Turtle()
turtle2=t.Turtle()
turtle3=t.Turtle()
turtle4=t.Turtle()
turtle5=t.Turtle()
turtle6=t.Turtle()
f_line=t.Turtle()

f_line.width(10)
f_line.showturtle()
f_line.teleport(500,-300)
f_line.setheading(90)
f_line.fd(600)

turtle1.color("red")
turtle2.color("orange")
turtle3.color("yellow")
turtle4.color("green")
turtle5.color("blue")
turtle6.color("purple")

turtle1.shape("turtle")
turtle2.shape("turtle")
turtle3.shape("turtle")
turtle4.shape("turtle")
turtle5.shape("turtle")
turtle6.shape("turtle")

turtle1.teleport(-500,250)
turtle2.teleport(-500,150)
turtle3.teleport(-500,50)
turtle4.teleport(-500,-50)
turtle5.teleport(-500,-150)
turtle6.teleport(-500,-250)

turtles=[turtle1,turtle2,turtle3,turtle4,turtle5,turtle6]


while True:
    for turtle in turtles:
        if int(turtle.xcor())>=500:
            if turtle==turtles[0]:
                print('RED WINS!')
                sys.exit()
            elif turtle==turtles[1]:
                print('ORANGE WINS!')
                sys.exit()
            elif turtle==turtles[2]:
                print('YELLOW WINS!')
                sys.exit()
            elif turtle==turtles[3]:
                print('GREEN WINS!')
                sys.exit()
            elif turtle==turtles[4]:
                print('BLUE WINS!')
                sys.exit()
            elif turtle==turtles[5]:
                print('PURPLE WINS!')
                sys.exit()
    chosen_turtle=random.choice(turtles)
    chosen_turtle.fd(random_forward)
