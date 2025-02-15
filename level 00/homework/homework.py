from turtle import*
speed(10)
width(4)

color("purple")
#ვხატავთ სახლის კედლებს

begin_fill()

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(180)

end_fill()


forward(200)
color("black")


#ვხატავთ სახურავს

begin_fill()

right(30)
forward(200)

right(120)
forward(200)

end_fill()

color("purple")

right(30)
forward(200)


#ვხატავთ კარებს

begin_fill()


right(90)
forward(75)



color("gray")

right(90)
forward(80)

left(90)
forward(50)

left(90)
forward(80)

end_fill()

penup()
goto(0,200)

#ვხატავთ ფანჯრებს

begin_fill()
color("skyblue")

pendown()
left(90)
forward(50)

right(90)
forward(50)
right(90)
forward(50)

end_fill()

#ვხატავთ მეორე ფანჯარას

penup()
goto(200,200)
pendown()
begin_fill()

forward(50)
left(90)
forward(50)
left(90)
forward(50)

end_fill()


exitonclick()