from snake_game_utils import make_screen, make_turtle_object,\
    change_food_pos, move_snake, go_up, go_down, go_right, go_left,\
    reset, wait, eat_apple, move_snake_bodies, check_body_collisions

snake_body = []
score = 0
high_score = 0
win = make_screen()
head = make_turtle_object("blue", "square")
food = make_turtle_object("red", "circle")
change_food_pos(food)

pen = make_turtle_object(color="white")
pen.hideturtle()
pen.goto(0, 260)
pen.write(f"Score : {score}, High Score: {high_score}",
          align="center", font=80)

border_pen = make_turtle_object(color="white")
border_pen.hideturtle()
border_pen.goto(-300,300)
border_pen.pensize(20)
border_pen.pendown()
for i in range(4):
    border_pen.forward(595)
    border_pen.right(90)

win.listen()
win.onkey(lambda: go_up(head), "Up")
win.onkey(lambda: go_down(head), "Down")
win.onkey(lambda: go_right(head), "Right")
win.onkey(lambda: go_left(head), "Left")

while True:
    win.update()
    score = eat_apple(head, food, snake_body, score, high_score, pen)

    move_snake_bodies(head, snake_body)
    if head.xcor() > 240 or head.xcor() < -240 or head.ycor() > 270 or head.ycor() < -280:
        reset(head, snake_body)
        score = 0
    move_snake(head)
    if check_body_collisions(head, snake_body):
        score = 0

    wait(0.2)
