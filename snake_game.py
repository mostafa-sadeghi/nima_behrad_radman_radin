import turtle
import time
from random import randint


snake_body = []


def make_turtle_object(color, shape):
    turtle_object = turtle.Turtle()
    turtle_object.speed("fastest")
    turtle_object.direction = "none"
    turtle_object.shape(shape)
    turtle_object.color(color)
    turtle_object.penup()
    return turtle_object


def change_food_pos():
    food_x_position = randint(-240, 240)
    food_y_position = randint(-240, 240)
    food.setposition(food_x_position, food_y_position)


def go_up():
    if head.direction != "down":
        head.direction = "up"


def go_down():
    if head.direction != "up":
        head.direction = "down"


def go_right():
    if head.direction != "left":
        head.direction = "right"


def go_left():
    if head.direction != "right":
        head.direction = "left"


def move_snake():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)


win = turtle.Screen()
win.title("Snake Game")
win.bgcolor("black")
win.setup(width=600, height=600)
win.tracer(0)

head = make_turtle_object("blue", "square")

food = make_turtle_object("red", "circle")
change_food_pos()


win.listen()
win.onkey(go_up, "Up")
win.onkey(go_down, "Down")
win.onkey(go_right, "Right")
win.onkey(go_left, "Left")


def reset():
    time.sleep(0.5)
    head.goto(0, 0)
    head.direction = ""
    for body in snake_body:
        body.ht()
    snake_body.clear()


while True:
    win.update()

    if head.distance(food) < 20:
        change_food_pos()
        new_tail = make_turtle_object("cyan", "square")
        snake_body.append(new_tail)
        print(snake_body)

    for i in range(len(snake_body) - 1, 0, -1):
        x = snake_body[i - 1].xcor()
        y = snake_body[i - 1].ycor()
        snake_body[i].setpos(x, y)
    if len(snake_body) > 0:
        xhead = head.xcor()
        yhead = head.ycor()
        snake_body[0].setpos(xhead, yhead)

    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        reset()

    move_snake()
    time.sleep(0.15)
