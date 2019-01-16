import turtle

wn = turtle.Screen()
wn.title('Pong Game by @Pankaj')
wn.bgcolor('black')
wn.setup(width=800, height=600)
wn.tracer(0)

#paddle_left
paddle_a = turtle.Turtle()
paddle_a.speed()
paddle_a.shape('square')
paddle_a.color('white')
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-340, 0)

#paddle_right
paddle_b = turtle.Turtle()
paddle_b.speed()
paddle_b.shape('square')
paddle_b.color('white')
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(340, 0)

#ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape('circle')
ball.color('white')
ball.penup()
ball.goto(0, 0)
ball.dx = 1/5
ball.dy = 1/5

#Score
score_a = 0
score_b = 0

#pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: {}  Player B: {}".format(score_a,score_b),align="center",font=("courier", 24, "normal"))

def paddle_a_up():
    y = paddle_a.ycor()
    if y >= 250:
        paddle_a.sety(250)
    else:
        paddle_a.sety(y+20)

def paddle_a_down():
    y = paddle_a.ycor()
    if y <= -250:
        paddle_a.sety(-250)
    else:
        paddle_a.sety(y-20)

def paddle_b_up():
    y = paddle_b.ycor()
    if y >= 250:
        paddle_b.sety(250)
    else:
        paddle_b.sety(y+20)

def paddle_b_down():
    y = paddle_b.ycor()
    if y <= -250:
        paddle_b.sety(-250)
    else:
        paddle_b.sety(y-20)

#KeyBinding
wn.listen()
wn.onkeypress(paddle_a_up, 'w')
wn.onkeypress(paddle_a_down, 's')
wn.onkeypress(paddle_b_up, 'Up')
wn.onkeypress(paddle_b_down, 'Down')

while True:
    wn.update()

    # move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # ball & paddle collison
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
        ball.setx(340)
        ball.dx = -1 * ball.dx

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40):
        ball.setx(-340)
        ball.dx = -1 * ball.dx


    #border checking
    if ball.ycor() >= 290:
        ball.dy = -1 * ball.dy

    if ball.ycor() <= -290:
        ball.dy = -1 * ball.dy

    if ball.xcor() >= 390:
        #ball.goto(0,0)
        ball.dx = -1 * ball.dx
        score_a += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a,score_b),align="center",font=("courier", 24, "normal"))
        if score_a >= 10:
            pen.clear()
            pen.write("Player A wins", align="center",
                      font=("courier", 24, "normal"))

    if ball.xcor() <= -390:
        #ball.goto(0, 0)
        ball.dx = -1 * ball.dx
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b),align="center",font=("courier", 24, "normal"))
        if score_b >= 10:
            pen.clear()
            pen.write("Player B wins", align="center",
                      font=("courier", 24, "normal"))






