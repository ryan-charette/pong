from random import randint
import turtle

play_window = turtle.Screen()
play_window.title("Pong")
play_window.bgcolor("black")
play_window.setup(width = 800, height = 600)
play_window.tracer(0)

left_paddle = turtle.Turtle()
left_paddle.speed(0)
left_paddle.shape("square")
left_paddle.shapesize(stretch_wid = 5, stretch_len = 1)
left_paddle.color("white")
left_paddle.penup()
left_paddle.goto(-370, 0)

right_paddle = turtle.Turtle()
right_paddle.speed(0)
right_paddle.shape("square")
right_paddle.shapesize(stretch_wid = 5, stretch_len = 1)
right_paddle.color("white")
right_paddle.penup()
right_paddle.goto(370, 0)

ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.x_velocity = randint(-5, 5) / 100
if ball.x_velocity < 0.02 and ball.x_velocity >= 0:
    ball.x_velocity = 0.02
elif ball.x_velocity < 0 and ball.x_velocity > -0.02:
    ball.x_velocity = -0.02
ball.y_velocity = randint(-5, 5) / 100

def left_paddle_up():
    y = left_paddle.ycor()
    y += 20
    left_paddle.sety(y)

def left_paddle_down():
    y = left_paddle.ycor()
    y -= 20
    left_paddle.sety(y)

def right_paddle_up():
    y = right_paddle.ycor()
    y += 20
    right_paddle.sety(y)

def right_paddle_down():
    y = right_paddle.ycor()
    y -= 20
    right_paddle.sety(y)

play_window.listen()
play_window.onkeypress(left_paddle_up, "w")
play_window.onkeypress(left_paddle_down, "s")
play_window.onkeypress(right_paddle_up, "Up")
play_window.onkeypress(right_paddle_down, "Down")

while True:
    play_window.update()

    ball.setx(ball.xcor() + ball.x_velocity)
    ball.sety(ball.ycor() + ball.y_velocity)

    if ball.ycor() > 290:
        ball.sety(290)
        ball.y_velocity *= -1
    elif ball.ycor() < -290:
        ball.sety(-290)
        ball.y_velocity *= -1
    
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.x_velocity *= -1
    elif ball.xcor() < -390:
        ball.goto(0, 0)
        ball.x_velocity *= -1
        
    if ball.xcor() > 360 and ball.xcor() < 370 and ball.ycor() < right_paddle.ycor() + 50 and ball.ycor() > right_paddle.ycor() - 50:
        ball.setx(360)
        ball.x_velocity *= -1
    elif ball.xcor() < -360 and ball.xcor() > -370 and ball.ycor() < left_paddle.ycor() + 50 and ball.ycor() > left_paddle.ycor() - 50:
        ball.setx(-360)
        ball.x_velocity *= -1