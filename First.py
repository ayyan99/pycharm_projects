import turtle
import time
import random

delay = 0.1

sc = 0          # sc for score
high_sc = 0



# setting up window
wn = turtle.Screen()
wn.title("Snake Game")
wn.bgcolor("green")
wn.setup(width=600, height=600)
wn.tracer(0)  # turns off screen updates

# snake head
head = turtle.Turtle()
head.speed(0)  # max animation speed is 0
head.shape("square")
head.color("black")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# snake food
food = turtle.Turtle()
food.speed(0)  # max animation speed is 0
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)

segments = []       #list segments for snake body

# score
score = turtle.Turtle()
score.speed(0)
score.shape("square")
score.color("white")
score.penup()
score.hideturtle()
score.goto(0, 260)
score.write("Your Score: 0  High Score: 0", align="center", font=("Courier", 20, "bold"))


# functions

def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

#linking to keyboard keys
wn.listen()
wn.onkey(go_up, 'Up')
wn.onkey(go_down, 'Down')
wn.onkey(go_left, 'Left')
wn.onkey(go_right, 'Right')


# main game loop

while True:
    wn.update()

    # check for snake body and border collision
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        time.sleep(0.5)
        head.goto(0, 0)
        head.direction = "stop"

        # hiding the segments
        for segment in segments:
            segment.goto(1000, 1000)

        # clearing the segments list
        segments.clear()            # or segments = []

        # resetting the score
        sc = 0

        # resetting the delay
        delay = 0.1

        score.clear()
        score.write("Your Score: {}  High Score: {}".format(sc, high_sc), align="center", font=("Courier", 20, "bold"))


    # checking for snake body and food collision
    if head.distance(food) < 20:

        # move the food to random spot
        x = random.randint(-260, 260)
        y = random.randint(-260, 260)
        food.goto(x, y)

        # add a segment to the snake body
        new_segment = turtle.Turtle()
        new_segment.speed(0)  # max animation speed is 0
        new_segment.shape("square")
        new_segment.color("black")
        new_segment.penup()
        segments.append(new_segment)

        # shorten the delay (as the length of snake increases, the snake moves faster)
        delay -= 0.001

        # increase the score
        sc += 5

        if sc >= high_sc:
            high_sc = sc

        score.clear()
        score.write("Your Score: {}  High Score: {}".format(sc, high_sc), align="center", font=("Courier", 20, "bold"))

    # move end segments in reverse order
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)

    # move segment 0 to where the head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    move()

    # check for head colliding with body
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(0.5)
            head.goto(0, 0)
            head.direction = "stop"

            # hiding the segments
            for segment in segments:
                segment.goto(1000, 1000)

            # clearing the segments list
            segments.clear()  # or segments = []

            # resetting the score
            sc = 0

            # resetting the delay
            delay = 0.1

            score.clear()
            score.write("Your Score: {}  High Score: {}".format(sc, high_sc), align="center",
                        font=("Courier", 20, "bold"))

    time.sleep(delay)

wn.mainloop()
