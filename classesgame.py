import turtle
import random
import math


wn = turtle.Screen()
wn.bgcolor("black")
wn.title("game using classes")


class Game(turtle.Turtle):
    
    def __init__(self):
        turtle.Turtle.__init__(self)                    
        self.penup()
        self.hideturtle()
        self.speed(0)
        self.color("white")
        self.goto(-290, 310)
        self.score = 0

    def updatescore(self):
        self.clear()
        self.write("Score: {}". format(self.score),False,align ="left", font=("Arial",14,"normal"))

    def changescore(self, points):
        self.score += points
        self.updatescore()
         


class Border(turtle.Turtle):
    def __init__(self):
         turtle.Turtle.__init__(self)
         self.penup()
         self.hideturtle()
         self.speed(0)
         self.color("white")
         self.pensize(5)
         
    def drawborder(self):
        self.penup()
        self.goto(-300, -300)
        self.pendown()
        self.goto(-300, 300)
        self.goto(300, 300)
        self.goto(300, -300)
        self.goto(-300, -300)


class Player(turtle.Turtle):
    
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.penup()
        self.shape("triangle")
        self.color("red")
        self.speed = 1

    def move(self):
        self.forward(self.speed)


        if self.xcor() > 290 or self.xcor() < -290:
            self.left(60)
        if self.ycor() > 290 or self.ycor() < -290:
            self.left(60)
        
    def turnleft(self):
        self.left(30)
        
    def turnright(self):
        self.right(30)

    def increasespeed(self):
        self.speed += 1

    def decreasespeed(self):
        self.speed -= 1


class Goal(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.penup()
        self.speed(0)
        self.shape("circle")
        self.color("green")
        self.speed = 2
        self.goto(random.randint(-250, 250), random.randint(-250, 250))
        self.setheading(random.randint(0, 360))

    def jump(self):
        self.goto(random.randint(-250, 250), random.randint(-250, 250))
        self.setheading(random.randint(0, 360))  


    def move(self):
        self.forward(self.speed)
        
    
        
        

        if self.xcor() > 290 or self.xcor() < -290:
            self.left(60)
        if self.ycor() > 290 or self.ycor() < -290:
            self.left(60)

def iscollision(t1,t2):
    a = t1.xcor()-t2.xcor()
    b = t1.ycor()-t2.ycor()
    distance = math.sqrt((a ** 2) + (b ** 2))


    if distance < 20:
        return True
    else:
        return False
    
        
#create class instances 
player = Player()
border = Border()
goal = Goal()
game = Game()


#draw border
border.drawborder()

goals = []
for count in range(6):
    goals.append(Goal())


#keybord bindings
turtle.listen()
turtle.onkey(player.turnleft, "Left")
turtle.onkey(player.turnright, "Right")
turtle.onkey(player.increasespeed, "Up")
turtle.onkey(player.decreasespeed, "Down")


wn.tracer(0)

#main loop 
while True:
    wn.update()
    player.move()
    goal.move()

    for goal in goals:
        goal.move()
        
    

    if iscollision(player, goal):
        goal.jump()
        game.changescore(10)
    
