import random

from turtle import Turtle,Screen
s=Screen()

ans=s.textinput("Make your bet!", "who will win the race?Enter a colour")

colours=["red","blue","pink","green","purple"]
turtle_list=[]


#turtle for heading
n=Turtle()
n.shape("turtle")
n.penup()
n.left(90)
n.hideturtle()
n.forward(230)
ws=n.write("Turtle race" , move=True,align='right',font=('Arial',15,'bold'))

#turtle for finish line
l=Turtle()
l.penup()
l.setposition(300,250)
l.pendown()
l.right(90)
l.hideturtle()
l.forward(500)


#creating turtle and setting them in their starting position
y=0
for i in colours:
    t=Turtle()
    t.shape("turtle")
    t.color(i)
    t.penup()
    t.goto(-280,100-y)
    y+=45
    turtle_list.append(t)

#the race starts if only you make a bet
race=False
if ans:
    race=True
while race:
    for i in turtle_list:
        i.speed("fastest")
        i.forward(random.randint(1,10))
        if i.xcor()>295:
            win=i.color()[0]
            race=False
            break

if ans==win:
    print(f"You won the bet!,{win} won the game")
else:
    print(f"try again!,{win} won the game")

s.exitonclick()