from turtle import Turtle, Screen
import time
import random

def create_snake(pos):
    snake_body = Turtle()
    snake_body.shape("square")
    snake_body.color("orangered")
    snake_body.up()
    snake_body.goto(pos)
    snakes.append(snake_body)

screen = Screen()
screen.setup(600,600)
screen.bgcolor("khaki")
screen.title("Snake Game")
screen.tracer(0)

# snake 만들기
start_pos = [(0,0), (-20,0), (-40,0)]
snakes =[]

for pos in start_pos:
    create_snake(pos)

screen.listen()
screen.onkeypress(up,"Up")

game_on = True
while game_on:
    screen.update()
    time.sleep(0,1)

    for i in range(len(snakes) -1, 0, -1):
        snakes[i].goto(snakes[i-1].pos())

    snakes[0].forward(10)
    
