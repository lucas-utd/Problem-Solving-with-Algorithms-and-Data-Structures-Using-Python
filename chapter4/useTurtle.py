from turtle import *

myTurtle = Turtle()
myWin = myTurtle.getscreen()


def drawSpiral(myTurtle, lineLen):
    if lineLen > 0:
        myTurtle.forward(lineLen)
        myTurtle.right(90)
        drawSpiral(myTurtle, lineLen - 5)


def tree(branchLen: int, t: Turtle) -> None:
    if branchLen > 5:
        t.forward(branchLen)
        t.right(20)
        tree(branchLen - 15, t)
        t.left(40)
        tree(branchLen - 10, t)
        t.right(20)
        t.backward(branchLen)


myTurtle.left(90)
myTurtle.up()
myTurtle.backward(300)
myTurtle.down()
myTurtle.color("green")
tree(110, myTurtle)
myWin.exitonclick()