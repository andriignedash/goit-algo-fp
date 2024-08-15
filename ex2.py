import turtle
import math

def draw_branch(t, branch_length, angle, level):
    if level == 0:
        return
    t.forward(branch_length)
    new_length = branch_length * 0.7
    t.left(angle)
    draw_branch(t, new_length, angle, level - 1)
    t.right(2 * angle)
    draw_branch(t, new_length, angle, level - 1)
    t.left(angle)
    t.backward(branch_length)

def draw_pythagoras_tree(level):
    window = turtle.Screen()
    window.bgcolor("white")
    t = turtle.Turtle()
    t.shape("turtle")
    t.color("brown")
    t.speed(0)
    t.penup()
    t.goto(0, -250)
    t.pendown()
    t.left(90)
    draw_branch(t, 100, 30, level)
    window.exitonclick()

level = int(input("Введіть рівень рекурсії для дерева Піфагора: "))
draw_pythagoras_tree(level)
