import turtle
import time
import random

delay = 0.2
score = 0
high_Score = 0

wn = turtle.Screen()
wn.title("snake")
wn.setup(width = 600, height = 600)
wn.bgcolor("green")
wn.tracer(0)

head = turtle.Turtle()
head.color("black")
head.shape("square")
head.penup()
head.goto(0,0)
head.speed(0)
head.direction = "up"



food = turtle.Turtle()
food.color("red")
food.shape("circle")
food.penup()

food.goto(0,100)
food.speed(0)
food.direction = "up"

seg = []
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("score: 0 high Score: 0",align= "center", font=("courier", 24 ,"normal"))
def go_up():
    
    if head.direction != "down":
        head.direction = "up"
def go_down():
    if head.direction != "up":
        head.direction = "down"    
def go_left():
    
    if head.direction != "right":
            head.direction = "left"    
def go_right():
    if head.direction != "left":
        head.direction = "right"
    
def move():
    
    if head.direction == "up":
        head.sety(y = head.ycor() + 20)
        
    if head.direction == "down":
        head.sety(y = head.ycor() -20)
        
    if head.direction == "left":
        head.setx(x = head.xcor() -20)
        
    if head.direction == "right":
        head.setx(x = head.xcor() +20)
          
wn.listen()
wn.onkeypress(go_up,"w")
wn.onkeypress(go_down,"s")
wn.onkeypress(go_left,"a")
wn.onkeypress(go_right,"d")
    

        
while True:
    wn.update()
    if head.distance(food) < 20:
       x =random.randint(-290,+290)
       y =random.randint(-290,+290)
       food.goto(x,y)
        

       new_seg = turtle.Turtle()
       new_seg.color("grey")
       new_seg.shape("square")
       new_seg.penup()
       new_seg.speed(0)
       seg.append(new_seg)
       score += 10
       if score > high_Score:
           high_Score = score
       pen.clear()    
       pen.write("score:{} high Score:{}".format(score,high_Score),align ="center",font=("courier" ,24,"normal"))    
    for index in range(len(seg)-1,0,-1):
         x = seg[index-1].xcor()
         y = seg[index-1].ycor()
         seg[index].goto(x,y)
    if len(seg) > 0:
        x = head.xcor()
        y = head.ycor()
        seg[0].goto(x,y)


    move()
    for segment in seg:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"
            for segment in seg:
                segment.goto(1000,1000)
            seg.clear()

            score = 0
            pen.clear()    
            pen.write("score:{} high Score:{}".format(score,high_Score),align ="center",font=("courier" ,24,"normal"))    
    time.sleep(delay)
wn.mainloop()    
