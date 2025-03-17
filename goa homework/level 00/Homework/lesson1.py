from turtle import *


#we want to paint a house 

#setp 1: draw a square

width(7)
color("red")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
#end of square

#drawing a door

forward(70)
color("yellow")
left(90)
forward(120)   #height of the door
right(90)
forward(60)
right(90)
forward(120)

#draw the roof
penup()
goto(200,200)
pendown()

color("blue")
right(150)
forward(200)
left(120)
forward(200)
#end drawing the roof


#draw left windows
penup()
goto(0,0)
left(120)
forward(10)
left(90)
forward(50)


pendown()
color("brown")
forward(70)
right(90)
forward(50)
right(90)
forward(70)
right(90)
forward(50)


penup()
goto(0,0)
left(180)
forward(35)
left(90)
forward(50)
pendown()
forward(70)

#draw right window
penup()
goto(0,0)
right(90)
forward(140)
left(90)
forward(50)
pendown()

forward(70)
right(90)
forward(50)
right(90)
forward(70)
right(90)
forward(50)
right(180)
forward(25)
left(90)
forward(70)
# end drawing windows

#end the lesson 1

exitonclick()