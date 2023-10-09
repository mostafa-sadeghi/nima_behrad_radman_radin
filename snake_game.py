from snake_game_utils import *

def on_close():
    global running
    running = False
snake_body = []
score = 0
high_score = 0
win = make_screen()
root = win._root
root.resizable(False, False)
root.protocol("WM_DELETE_WINDOW", on_close)

head = make_turtle_object("blue", "square")
food = make_turtle_object("red", "circle")
change_food_pos(food)

bomb = make_turtle_object("darkgreen", "circle")
change_food_pos(bomb)

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



running = True
while running:
    win.update()
    score,high_score = eat_apple(head, food, snake_body, score, high_score, pen)

    if head.distance(bomb)<20:
        score -= 1
        change_food_pos(bomb)
        if len(snake_body)>0:
            snake_body[-1].ht()
            del snake_body[-1]

    move_snake_bodies(head, snake_body)
    # if head.xcor() > 240 or head.xcor() < -240 or head.ycor() > 270 or head.ycor() < -280:
    #     reset(head, snake_body)
    #     score = 0

    if head.xcor() > 280:
        head.setx(-280)


    move_snake(head)
    if check_body_collisions(head, snake_body):
        score = 0

    wait(0.2)
