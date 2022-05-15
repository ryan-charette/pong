import turtle
from random import randint
import time

play_window = turtle.Screen()
play_window.title("Pong")
play_window.bgcolor("black")
play_window.setup(width = 800, height = 600)
play_window.tracer(0)

left_score = 0
right_score = 0

score = turtle.Turtle()
score.speed(0)
score.color("white")
score.penup()
score.hideturtle()
score.goto(0, 210)
score.write("0       0", align = "center", font = ("Courier", 50, "normal"))

divider = turtle.Turtle()
divider.speed(0)
divider.color("white")
divider.right(90)
divider.penup()
divider.goto(0, 300)
divider.pendown()
for dash in range(31):
    divider.forward(15)
    divider.penup()
    divider.forward(5)
    divider.pendown()

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
ball.x_velocity = randint(-10, 10) / 100
if ball.x_velocity < 0.05 and ball.x_velocity >= 0:
    ball.x_velocity = 0.05
elif ball.x_velocity < 0 and ball.x_velocity > -0.05:
    ball.x_velocity = -0.05
ball.y_velocity = randint(-10, 10) / 100
if ball.y_velocity == 0:
    ball.y_velocity = 0.01

def left_paddle_up():
    y = left_paddle.ycor()
    if y < 190:
        y += 60
        left_paddle.sety(y)
    else:
        left_paddle.sety(250)

def left_paddle_down():
    y = left_paddle.ycor()
    if y > -190:
        y -= 60
        left_paddle.sety(y)
    else:
        left_paddle.sety(-250)

def right_paddle_up():
    y = right_paddle.ycor()
    if y < 190:
        y += 60
        right_paddle.sety(y)
    else:
        right_paddle.sety(250)
def right_paddle_down():
    y = right_paddle.ycor()
    if y > -190:
        y -= 60
        right_paddle.sety(y)
    else:
        right_paddle.sety(-250)

play_window.listen()
play_window.onkeypress(left_paddle_up, "w")
play_window.onkeypress(left_paddle_down, "s")
play_window.onkeypress(right_paddle_up, "Up")
play_window.onkeypress(right_paddle_down, "Down")

while left_score < 6 and right_score < 6:
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
        ball.x_velocity = -1 * randint(5, 10) / 100
        left_score += 1
        score.clear()
        score.write("{}      {}".format(left_score, right_score), align = "center", font = ("Courier", 50, "normal"))

    elif ball.xcor() < -390:
        ball.goto(0, 0)
        ball.x_velocity = randint(5, 10) / 100
        right_score += 1
        score.clear()
        score.write("{}      {}".format(left_score, right_score), align = "center", font = ("Courier", 50, "normal"))
        
    if ball.xcor() > 360 and ball.xcor() < 370 and ball.ycor() < right_paddle.ycor() + 50 and ball.ycor() > right_paddle.ycor() - 50:
        ball.setx(360)
        if ball.x_velocity < 1:
            ball.x_velocity *= -1.5
        else:
            ball.x_velocity *= -1
    elif ball.xcor() < -360 and ball.xcor() > -370 and ball.ycor() < left_paddle.ycor() + 50 and ball.ycor() > left_paddle.ycor() - 50:
        ball.setx(-360)
        if ball.x_velocity < 1:
            ball.x_velocity *= -1.5
        else:
            ball.x_velocity *= -1
    if left_score == 6 or right_score == 6:
        score.clear()
        score.write("GAME OVER", align = "center", font = ("Courier", 50, "normal"))
        time.sleep(2)