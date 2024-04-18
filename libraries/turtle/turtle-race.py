import turtle
import random

# Set up screen
screen = turtle.Screen()
screen.title("Turtle Race")
screen.bgcolor("white")
screen.setup(width=600, height=400)

# Draw finishing line
finish_line = turtle.Turtle()
finish_line.penup()
finish_line.goto(250, 200)
finish_line.pendown()
finish_line.goto(250, -200)

# Create turtles
colors = ["red", "blue", "green", "orange", "purple", "black"]
turtles = []

for color in colors:
    new_turtle = turtle.Turtle()
    new_turtle.shape("turtle")
    new_turtle.color(color)
    turtles.append(new_turtle)

# Set starting positions
start_x = -250
start_y = 100

for turtle in turtles:
    turtle.penup()
    turtle.goto(start_x, start_y)
    start_y -= 40

# Race
while True:
    for turtle in turtles:
        turtle.forward(random.randint(1, 10))
        if turtle.xcor() >= 250:
            winner_color = turtle.color()[0]
            screen.title(f"{winner_color.capitalize()} turtle wins!")
            break
    else:
        continue
    break

screen.mainloop()