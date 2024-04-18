import turtle
import random

screen = turtle.Screen()
screen.tracer(0)
screen.bgcolor("black")

boundaryT = turtle.Turtle()
boundaryT.color("blue")
boundaryT.speed(0)
boundaryT.penup()
boundaryT.goto(-250,250)
boundaryT.pendown()
boundaryT.begin_fill()

for x in range(4):
  boundaryT.forward(500)
  boundaryT.right(90)
  boundaryT.begin_fill()
boundaryT.end_fill()
boundaryT.ht()

screen.update()

scoreT = turtle.Turtle()
scoreT.color("light steel blue")
scoreT.speed(0)
scoreT.penup()
scoreT.goto(-250,260)
score = 0
scoreT.write("Score: " + str(score), font=("Fixedsys",12,"normal"))
scoreT.ht()


player = turtle.Turtle()
player.penup()
player.goto(-100,-240)
player.color("deep pink")

screen.register_shape("paddle",((0,0),(20,0),(20,100),(0,100)))
player.shape("paddle")

ball = turtle.Turtle()
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(-50,-210)
ball.setheading(random.randint(1,179))

screen.update()

screen.register_shape("brick",((0,0),(10,0),(10,50),(0,50)))

colors = ["sky blue", "tomato", "lime green","yellow"]
def makeRow(x,y,colors):
  index = random.randint(0,len(colors)-1)
  row = []
  for i in range(8):
    targetT = turtle.Turtle()
    targetT.speed(0)
    targetT.shape("brick")
    targetT.color(colors[index])
    targetT.penup()
    targetT.goto(x + 60*i,y)
    targetT.pendown()
    row.append(targetT)
    index = random.randint(0,len(colors)- 1)
  return row


screen.update()


def right():
  player.forward(10)

screen.onkey(right, "Right")

def left():
  player.backward(10)

screen.onkey(left, "Left")

screen.listen()


def checkCollisonBrick(obj):
  if abs(ball.xcor() - obj.xcor()) < 50 and obj.ycor() <= ball.ycor() <= obj.ycor() + 10 :
    print("colided with the brick:", obj)
    return True
  return False

def checkCollisonPaddle(obj):
  if abs(ball.xcor() - obj.xcor()) < 100 and (obj.ycor() <= ball.ycor() <= obj.ycor() + 20) :
    return True

  return False

def bounce(context):
  if context == "top" or context == "paddle":
    ball.setheading(360 - ball.heading())
  elif 180 > ball.heading() >= 0:
    ball.setheading(180 - ball.heading())
  elif 180 <= ball.heading() < 360:
    ball.setheading(540 - ball.heading())

screen.update()

def countList():
  count = []
  for i in range(8):
    count.append(0)
  return count

def hitBrick(row, count, goal):
  global score
  for x in range(len(row)):  
    if checkCollisonBrick(row[x]):
    
      if count[x] > goal:
        row[x].ht()
        row[x].penup()
        row[x].goto(-1000,1000)
      else:     
        count[x] += 1
        bounce("paddle")

      score = updateScore(score)

  return count

def updateScore(score):
  score += 5
  scoreT.clear()
  scoreT.write("Score: " + str(score), font=("Fixedsys",12,"normal"))
  return score

row1 = makeRow(-230,200,colors)
count1 = countList()
row2 = makeRow(-230,170,colors)
count2 = countList()
row3 = makeRow(-230,140,colors)
count3 = countList()
row4 = makeRow(-230,110,colors)
count4 = countList()

gameContinue=True


while gameContinue:
  ball.forward(5)

  screen.update()

  count1 = hitBrick(row1, count1, 4)

  count2 = hitBrick(row2, count2, 3)

  count3 = hitBrick(row3, count3, 2)

  count4 = hitBrick(row4, count4, 1)



  if ball.ycor() < -240:
    boundaryT.penup()
    boundaryT.goto(-200,0)
    boundaryT.color("midnight blue")
    boundaryT.write("YOU LOSE! :( ", font=("Fixedsys",48,"normal"))
    gameContinue=False

  if score == 720:
    boundaryT.penup()
    boundaryT.goto(-200,0)
    boundaryT.color("orange")
    boundaryT.write("You Win!!! :)", font=("Fixedsys",48,"normal"))
    gameContinue=False

  

  if ball.xcor() > 240:
    bounce("right")

  if ball.xcor() < -240:
    bounce("left")


  if ball.ycor() > 240:
    bounce("top")


  if checkCollisonPaddle(player):
    bounce("paddle")

  if player.xcor() + 100  > 240:
    player.backward(10)

  
  if player.xcor() < -240:
    player.forward(10)


  screen.update()