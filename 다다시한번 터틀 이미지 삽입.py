import turtle # 터틀 그래픽 모듈을 불러온다.
import random # 난수 모듈을 불러온다.

screen = turtle.Screen()
image1 = "rabbit.gif"
image2 = "turtle.gif"

screen.addshape(image1)
screen.addshape(image2)

t1 = turtle.Turtle() # 첫 번째 거북이를 생성한다.
t1.shape(image1)
t2 = turtle.Turtle() # 두 번째 거북이를 생성한다.
t2.shape(image2)
