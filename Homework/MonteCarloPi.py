import math
import random
import turtle

def drawRedBox(z, width, height):
	z.fillcolor("red")
	z.width(1)
	z.begin_fill()
	z.forward(width)
	z.right(90)
	z.forward(height)
	z.right(90)
	z.forward(width)
	z.right(90)
	z.forward(height)
	z.end_fill()

def _montePi(count, endX, endY):	
	j = turtle.Screen()
	j.setworldcoordinates(0,0,endX,endY)
	j = turtle.Turtle()
	j.speed(10)
	j.penup()
	j.goto(endX * .25,endY * .75)
	j.setheading(0)
	j.pendown()
	drawRedBox(j, endX//2,endY//2)
	j.penup()
	j.goto(endX*.75,endY//2)
	j.pendown()
	j.fillcolor("green")
	j.width(1)
	j.begin_fill()
	j.circle(endX/2/2)
	j.end_fill()
	j.penup()
	j.goto(endX//2,endY*.75)
	j.pendown()
	j.width(5)
	j.setheading(270)
	j.forward(endY//2)
	j.penup()
	j.goto(endX*.25,endY//2)
	j.pendown()
	j.setheading(0)
	j.forward(endX//2)
	j.penup()
	dartsInCircle = 0
	j.speed(0)
	for i in range(count):
		x = random.randint(endX*.25,endY * .75)
		y = random.randint(endX*.25,endY * .75)
		j.goto(x,y)
		j.dot(10, "black")
		d = math.sqrt(x**2 + y**2)
		if d <= endX*.8419:
			dartsInCircle +=1
	print(dartsInCircle)
	j.speed(100)
	piee = 4 * dartsInCircle / count
	strrr = str(piee)
	j.penup()
	j.goto(endX//2,endY*.8)
	j.pendown()
	j.color('deep pink')
	style = ('Courier', 30, 'italic')
	j.write("Pi = " + strrr, font=style, align='center')

	
_montePi(500,200,200)
input()



