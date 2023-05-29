import turtle
import time


def go_up():
    if head.direction != "down":
        head.direction = "up"


def move_snake():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    # TODO add left and right move functionality


win = turtle.Screen()
win.title("Snake Game")
win.bgcolor("black")
win.setup(width=600, height=600)


head = turtle.Turtle()
head.speed("fastest")
head.direction = "none"
head.shape("square")
head.color("blue")
head.penup()

win.listen()
win.onkey(go_up, "Up")


while True:
    win.update()
    move_snake()
    time.sleep(0.15)
