import turtle
from random import seed,randrange
seed(20)

wn=turtle.Screen()
wn.title("Snake")
wn.bgcolor("black")
wn.setup(width=800,height=640)
wn.tracer(0)

# Snake
snake=turtle.Turtle()
snake.speed(0)
snake.shape("square")
snake.color("white")
snake.penup()
snakesize=1
snakecoords=[]

# Snake shadow
shadow=turtle.Turtle()
shadow.speed(0)
shadow.shape("square")
shadow.color("black")
shadow.penup()
shadow.ht()

# Apple
apple=turtle.Turtle()
apple.speed(0)
apple.shape("square")
apple.color("red")
apple.penup()

# Temporary
# You dead sign
sign=turtle.Turtle()
sign.speed(0)
sign.color("white")
sign.penup()
sign.hideturtle()
sign.goto(0,260)


# Apple spawn
def apple_spawn():
    apple.goto(randrange(-400,400,20),randrange(-320,320,20))


# Snake movement
def snake_up():
    snake.stamp()
    snakecoords.append((snake.xcor(),snake.ycor()))
    snake.sety(snake.ycor()+20)

def snake_down():
    snake.stamp()
    snakecoords.append((snake.xcor(),snake.ycor()))
    snake.sety(snake.ycor()-20)

def snake_right():
    snake.stamp()
    snakecoords.append((snake.xcor(),snake.ycor()))
    snake.setx(snake.xcor()+20)

def snake_left():
    snake.stamp()
    snakecoords.append((snake.xcor(),snake.ycor()))
    snake.setx(snake.xcor()-20)


# Snake death check
def snakedeath():
    for xcor,ycor in snakecoords:
        if snake.xcor()==xcor and snake.ycor()==ycor:
            return True
    return False

# Keyboard binding
wn.listen()
wn.onkeypress(snake_up,"w")
wn.onkeypress(snake_down,"s")
wn.onkeypress(snake_right,"d")
wn.onkeypress(snake_left,"a")

while True:
    wn.update()
    # Snake death/ border checking
    if snake.xcor()>380 or snake.xcor()<-380 or snake.ycor()>300 or snake.ycor()<-300 or snakedeath():
        sign.write("YOU DIED", align="center", font=("Courier", 24, "normal"))


    # Apple refresh spawn
    if (snake.xcor()==apple.xcor()) and (snake.ycor()==apple.ycor()):
        snakesize+=1
        apple_spawn()

    # Snake body length checker
    if len(snakecoords)>=snakesize:
        shadowx,shadowy=snakecoords[0]
        shadow.goto(shadowx,shadowy)
        shadow.stamp()
        del snakecoords[0]