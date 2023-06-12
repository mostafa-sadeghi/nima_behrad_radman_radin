from turtle import Screen, Turtle
from random import randint
import time


def make_screen():
    surface = Screen()
    surface.title("Snake Game")
    surface.bgcolor("black")
    surface.setup(width=600, height=600)
    surface.tracer(0)
    return surface


def make_turtle_object(color="black", shape="square"):
    turtle_object = Turtle()
    turtle_object.speed("fastest")
    turtle_object.direction = "none"
    turtle_object.shape(shape)
    turtle_object.color(color)
    turtle_object.penup()
    return turtle_object


def change_food_pos(food):
    food_x_position = randint(-240, 240)
    food_y_position = randint(-240, 240)
    food.setposition(food_x_position, food_y_position)


def move_snake(head):
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


def reset(head, snake_body):
    time.sleep(0.5)
    head.goto(0, 0)
    head.direction = ""
    for body in snake_body:
        body.ht()
    snake_body.clear()


def go_up(head):
    if head.direction != "down":
        head.direction = "up"


def go_down(head):
    if head.direction != "up":
        head.direction = "down"


def go_right(head):
    if head.direction != "left":
        head.direction = "right"


def go_left(head):
    if head.direction != "right":
        head.direction = "left"


def wait(secs):
    time.sleep(secs)


def eat_apple(head, food, snake_body, score, high_score, pen):

    if head.distance(food) < 20:
        score += 1

        change_food_pos(food)
        new_tail = make_turtle_object("cyan", "square")
        snake_body.append(new_tail)
    pen.clear()
    pen.write(f"Score : {score}, High Score: {high_score}",
              align="center", font=80)
    return score


def move_snake_bodies(head, snake_body):
    for i in range(len(snake_body) - 1, 0, -1):
        x = snake_body[i - 1].xcor()
        y = snake_body[i - 1].ycor()
        snake_body[i].setpos(x, y)
    if len(snake_body) > 0:
        xhead = head.xcor()
        yhead = head.ycor()
        snake_body[0].setpos(xhead, yhead)


def check_body_collisions(head, snake_body):
    for body in snake_body:
        if body.distance(head) < 20:
            reset(head, snake_body)
            return True
