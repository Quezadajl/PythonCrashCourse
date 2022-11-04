import turtle

wn = turtle.Screen()
wn.title("Pong by @Joselit!")
wn.bgcolor("black")
wn.setup(width=800, height=600)
#pixel usage
wn.tracer(0)

# Score
score_a = 0
score_b = 0

#Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)#speed of animation;Maximum
paddle_a.shape("square")#There are other built-in shapes; circle/square...
paddle_a.color("blue")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)



#Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)#speed of animation;Maximum
paddle_b.shape("square")#There are other built-in shapes; circle/square...
paddle_b.color("green")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(+350, 0)


#Ball
ball = turtle.Turtle()
ball.speed(-1000) #speed of animation;Maximum
ball.shape("circle") #There are other built-in shapes; circle/square...
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 2
ball.dy = -2


# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("red")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0 Player: 0", align="center", font=("Courier", 24, "normal"))



# Function
##* movements of the paddles
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20 #allows it to move by pixels per press(like a coordinate grid)
    paddle_a.sety(y)
    
def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20 #allows it to move by pixels per press(like a coordinate grid)
    paddle_a.sety(y)
    
def paddle_b_up():
    y = paddle_b.ycor()
    y += 20 #allows it to move by pixels per press(like a coordinate grid)
    paddle_b.sety(y)
    
def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20 #allows it to move by pixels per press(like a coordinate grid)
    paddle_b.sety(y)
    
#keyboard binding

wn.listen()
wn.onkeypress(paddle_a_up,"w")
wn.onkeypress(paddle_a_down,"s")
wn.onkeypress(paddle_b_up,"Up")
wn.onkeypress(paddle_b_down,"Down")
    

# Main game loop

while True:
    wn.update()
    
    #move the ball
    ball.setx(ball.xcor() + (ball.dx / 4))
    ball.sety(ball.ycor() + (ball.dy / 4))
    
    # Border Checking; reverses the direction of the ball
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
    
    if ball.xcor() > 390: #right side of the screen
        ball.goto(0,0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {} Player: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        
    if ball.xcor() < -390: #Left side of the screen
        ball.goto(0,0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {} Player: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        
    # Paddle and ball collisions
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1
        
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1