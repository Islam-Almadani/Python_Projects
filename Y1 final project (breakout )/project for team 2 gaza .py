import turtle 
import random 

turtles = []

screen = turtle.Screen()


boundary = 200
box_size = 400
brick_width = 20
x_gap_size = 10
y_gap_size = 10
# to make the mox 
t = turtle.Turtle()
t.pensize(3)
t.speed(0)
t.pencolor("red")
t.hideturtle()
t.pu()
t.goto(boundary,-boundary)
t.pd()
t.left(90)
for i in range(4):
  t.fd(400)
  t.left(90)


# to make the paddle 
paddle = turtle.Turtle()
paddle.hideturtle()
paddle.shape("square")
paddle.shapesize(0.5,3.5)
paddle.fillcolor("sky blue")
paddle.color("sky blue")
paddle.pu()
paddle.goto(0,-boundary+20)
paddle.showturtle()
# to make the paddle move right and lift , and don't go out side the box  

def move_right():
  if paddle.xcor()  < 160:
    paddle.speed(0)
    paddle.pu()
    paddle.fd(20)
  # if t1.xcor == box_size :


def move_left():
  if paddle.xcor()  > -160:
    paddle.speed(0)
    paddle.pu()
    paddle.back(20)

screen.onkey(move_right,"Right")
screen.onkey(move_left,"Left")
screen.listen()
# to make one row of bricks on the scree 
def make_brick_row ():
  boundary = 200
  box_size = 400
  x_brick_width = 20
  Y_brick_width = 39
  x_gap_size = 10
  y_gap_size = 10
  cloers = ['red' ,'green' , 'blue' , 'yellow']
  for j in range (4): 
    x_gap_size = 10

    for i in range (8):
      r = turtle.Turtle()
      r.fillcolor(cloers[j])
      r.color(cloers[j])
      r.speed(0)
      r.hideturtle()
      r.pu()
      r.shape("square")
      r.shapesize(1,1.95)
      r.goto((-boundary + x_gap_size + x_brick_width ),(boundary - y_gap_size - x_brick_width/2 )) 
      r.showturtle()

      x_gap_size += 39+10
      turtles.append(r)
    y_gap_size +=20+10

make_brick_row()


def is_collided_with(a, b):
    # return abs(a.xcor()  - b.xcor() ) < 5 and abs(a.ycor()  - b.ycor() ) < 5
    return a.distance(b) <20 

angles = [50,135,-30,-110,70 , 20 ]
angle = random.choice(angles)

score = 0   

ball = turtle.Turtle()
ball.shape("circle") 
ball.shapesize(0.8)
ball.seth(angle)
ball.pu()
ball.speed(0)
v = 0
score_t = turtle.Turtle()
score_t.pu()
score_t.hideturtle()
score_t.goto(-200,200)
score_t.write("Your score = {}".format(score) ,font=("Arial", 10 , "normal"))


ball_speed = 2.5
secands = 0 
miniuts = 3 


time1 = turtle.Turtle()
time1.pu()
time1.hideturtle()
time1.goto(100,200)

minutes = 0 
secands = 0 
def time () : 
  global secands 
  global minutes
  if secands == 60 : 
    secands -= 60 
    minutes += 1 
  secands += 1
  if len(str(secands)) < 2 :
    timer = "The Timer = 0{}:0{}".format(minutes,secands)
  else :
    timer = "The Timer = 0{}:{}".format(minutes,secands)
  time1.clear()
  time1.write(timer,font=("Arial", 10 , "normal"))

  turtle.ontimer(time,1000)
time ()

while v == 0 :

  ball.fd(ball_speed)
  for x in turtles:

   if is_collided_with(x,ball):
    x.hideturtle()
    turtles.remove(x)
    angle = 360 - angle 
    ball.seth(angle) 
    score += 10
    score_t.clear()
    score_t.write("Your score = {}".format(score) ,font=("Arial", 10 , "normal"))

  if score >= 80 :
    ball_speed = 3 
  if score >= 160 :
    ball_speed = 3.5
  if score >= 280 :
    ball_speed = 4
  

  if ball.xcor() -10 <= -200 :
    angle = 180 - angle
    ball.seth(angle) 
  if ball.xcor() +10 >= 200 :
    angle = 180 - angle
    ball.seth(angle) 
  if ball.ycor() +10 >= 200 :
    angle = 360 - angle 
    ball.seth(angle) 
  if ball.ycor() -10 <= paddle.ycor()+5 and (ball.xcor() +10 >= paddle.xcor()-30  and ball.xcor() +10 <= paddle.xcor()+40):
    angle = 360 - angle
    ball.seth(angle) 

  if ball.ycor() -10 <=-200:
    ball.goto(-150,-80)
    ball.write("You lose ! \nYour score \n       {}".format(score) , score,font=("Arial", 50 , "normal"))
    v = 1
    ball.hideturtle()
  if len(turtles) <= 4 :
    turtles[0].goto(-170,180)
    turtles[1].goto(-170,150)
    turtles[2].goto(-170,120)
    turtles[3].goto(-170,90)

    while v == 0 :
      for x in turtles :
        x.fd(2)
      
      if len(turtles) == 4 :
        if turtles[0].xcor() >= 150 :
          turtles[0].goto (-170,180)
        if turtles[1].xcor() >= 150 :
          turtles[1].goto (-170,150)
        if turtles[2].xcor() >= 150 :
          turtles[2].goto (-170,120)
        if turtles[3].xcor() >= 150 :
          turtles[3].goto (-170,90)
          ball_speed = 15
      if len(turtles) == 3 :
        if turtles[0].xcor() >= 150 :
          turtles[0].goto (-170,180)
        if turtles[1].xcor() >= 150 :
          turtles[1].goto (-170,150)
        if turtles[2].xcor() >= 150 :
          turtles[2].goto (-170,120)
        ball_speed = 9

      if len(turtles) == 2 :
        if turtles[0].xcor() >= 150 :
          turtles[0].goto (-170,180)
        if turtles[1].xcor() >= 150 :
          turtles[1].goto (-170,150)
        ball_speed = 8

      if len(turtles) == 1 :
        if turtles[0].xcor() >= 150 :
          turtles[0].goto (-170,180)
        ball_speed = 5
 
          
      ball.fd(ball_speed)
      for x in turtles:

       if is_collided_with(x,ball):
        x.hideturtle()
        turtles.remove(x)
        angle = 360 - angle 
        ball.seth(angle) 
        score += 10
        score_t.clear()
        score_t.write("Your score = {}".format(score) ,font=("Arial", 10 , "normal"))

      if score >= 400 :
        ball_speed = 3 
      if score >= 800 :
        ball_speed = 3.3
      if score >= 1200 :
        ball_speed = 3.8
      

      if ball.xcor() -10 <= -200 :
        angle = 180 - angle
        ball.seth(angle) 
      if ball.xcor() +10 >= 200 :
        angle = 180 - angle
        ball.seth(angle) 
      if ball.ycor() +10 >= 200 :
        angle = 360 - angle 
        ball.seth(angle) 
      if ball.ycor() -10 <= paddle.ycor()+5 and (ball.xcor() +10 >= paddle.xcor()-30  and ball.xcor() +10 <= paddle.xcor()+40):
        angle = 360 - angle
        ball.seth(angle) 
      if turtles == [] :
        ball.goto(-150,-120)
        ball.write("You win !\nYour score\n      {}".format(score) , score,font=("Arial", 50 , "normal"))
        ball.hideturtle()
        v = 1

      if ball.ycor() -10 <=-200:
        ball.goto(-130,-30)
        ball.write("You lose !\nYour score\n      {}".format(score) , score,font=("Arial", 50 , "normal"))
        v = 1
        ball.hideturtle()
        lenght = 180

turtle.done()

