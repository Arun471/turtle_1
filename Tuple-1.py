from turtle import Turtle, Screen

col = ('red', 'blue', 'green', 'yellow', 'pink', 'cyan')

t = Turtle()
screen = Screen()
screen.bgcolor('black')
t.speed(30)

for i in range(100):
    t.color(col[i % 6])
    t.forward(i*4)
    t.left(150)
    t.width(2)
