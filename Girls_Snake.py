# Girl Snake
# Import Libraries
import turtle
import pygame
import time
import random

# Create a Pygame mixer for sound effects
pygame.mixer.init()

# Time delay setup
delay = 0.1

# Score
score = 0
high_score = 0

# Load the sound for score change
score_sound = pygame.mixer.Sound("XXX/pp.wav")

# Load the sound for when the food is hit
food_sound = pygame.mixer.Sound("XXXX/bgg.wav")

# Load the background music
pygame.mixer.music.load("XXX/HarmBox.wav")

# Play the background music on a loop
pygame.mixer.music.play(-1)

# Setup the game window
gw = turtle.Screen()
gw.title("Girls Snake")
gw.bgcolor("cyan")
gw.setup(width=650, height = 650)
gw.tracer(0) # Turns off screen updates)

# Snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("magenta")
head.penup()
head.goto(0,0)
head.direction = "up"

# Create custom star shape to use as snake food
star_shape = ((0, 0), (-3, 7), (-9, 7), (-4, 12), (-7, 18), (0, 14), (7, 18), (4, 12), (9, 7), (3, 7))
turtle.register_shape("star", shape=star_shape)
turtle.shape("star")
turtle.hideturtle()

# Snake food
food = turtle.Turtle()
food.speed(0)
food.shape("star")
food.color("yellow")
food.penup()
food.goto(0,200)

segments = []

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("black")
pen.penup()
pen.hideturtle()
pen.goto(0, 290)
pen.write("Score: 0    High Score: 0", align="center", font=("Impact", 24, "normal"))

# Change the background color to cyan
gw.bgcolor("cyan")

# Draw and fill a green rectangle inside the white background
frame = turtle.Turtle()
frame.speed(0)
frame.color("green")
frame.penup()
frame.goto(-290, -290)
frame.begin_fill()  # Begin filling the rectangle
frame.pendown()
frame.pensize(4)
for _ in range(4):
    frame.forward(580)
    frame.left(90)
frame.end_fill()  # End filling the rectangle
frame.hideturtle()

# Functions
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

# Keyboard bindings
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

# Bind the arrow keys to the corresponding functions
gw.listen()
gw.onkeypress(go_up, "Up")
gw.onkeypress(go_down, "Down")
gw.onkeypress(go_left, "Left")
gw.onkeypress(go_right, "Right")

# Main game loop
while True:
    gw.update()

    # Check for a collision with the border
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"
        score_sound.play()

        # Hide the segments
        for segment in segments:
            segment.goto(1000, 1000)

        # Clear the segments list
        segments.clear()

        # Reset the score
        score = 0

        if score == 0:
            score_sound.play()

        # Reset the delay
        delay = 0.1

        pen.clear()
        pen.write("Score: {} High Score: {}".format(score, high_score), align="center", font= ("Impact", 24, "normal"))

    # Check for a collision with the food
    if head.distance(food) < 20:
        # Move the food to a new random spot 
        x= random.randint(-280,280)
        y= random.randint(-280, 280)
        food.goto(x,y)

        # Play the food hit sound
        food_sound.play()

        # Add a segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)

        # Shorten the delay
        delay -= 0.001

        # Increase the score
        score += 10

        if score > high_score:
            high_score = score

    pen.clear()
    pen.write("Score: {} High Score: {}".format(score, high_score), align="center", font= ("Impact", 24, "normal"))

    # Move the end segments first in reverse order
    for index in range(len(segments) -1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)

    # Move segment zero to where the head is at
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y) 

    move()
    time.sleep(delay)

    # Check for head collision with the body segments
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"

            # Hide the segments
            for segment in segments:
                segment.goto(1000, 1000)

            # Clear the segments list
            segments.clear()

            # Reset the score
            score = 0

            # Reset the delay
            delay = 0.1

            # Update the score display
            pen.clear()
            pen.write("Score: {} High Score: {}".format(score, high_score), align="center", font= ("Impact", 24, "normal"))

gw.mainloop()