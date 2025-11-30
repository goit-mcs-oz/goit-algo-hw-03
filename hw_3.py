# Завдання 3

from dataclasses import dataclass
import time
import turtle


class Stack:
    def __init__(self):
        self.stack = []

    def __str__(self):
        return str(self.stack)

    # Додавання елемента до стеку
    def push(self, item):
        self.stack.append(item)

    # Видалення елемента зі стеку
    def pop(self):
        if len(self.stack) < 1:
            return None
        return self.stack.pop()

    # Перевірка, чи стек порожній
    def is_empty(self):
        return len(self.stack) == 0

    # Перегляд верхнього елемента стеку без його видалення
    def peek(self):
        if not self.is_empty():
            return self.stack[-1]


@dataclass
class Disk:
    n: int


# Кількість дисків на початковому стрижні
n = 3

a = Stack()
for i in reversed(range(1, n + 1)):
    a.push(Disk(i))

b = Stack()
c = Stack()


def moveDisc(from_s: Stack, to_s: Stack):
    disk_from = from_s.peek()
    disk_to = to_s.peek()
    if disk_from and not disk_to:
        from_s.pop()
        to_s.push(disk_from)
    if disk_from and disk_to and disk_from.n < disk_to.n:
        from_s.pop()
        to_s.push(disk_from)

    redraw_towers()
    print(f"A:{a}, B:{b}, C:{c}")


def move(s, a, b, c):
    if s == 1:
        moveDisc(a, c)
        return
    else:
        move(s-1, a, c, b)
        moveDisc(a, c)
        move(s-1, b, a, c)


screen = turtle.Screen()
screen.setup(800, 500)
screen.title("Hanoi Towers Animation")
screen.tracer(0)

BASE_Y = -180
PEG_X = [-250, 0, 250]
DISC_HEIGHT = 22


def draw_peg(x):
    t = turtle.Turtle(visible=False)
    t.penup()
    t.goto(x, BASE_Y)
    t.pendown()
    t.pensize(6)
    t.goto(x, BASE_Y + 250)


def redraw_towers():
    screen.clear()
    screen.tracer(0)

    for x in PEG_X:
        draw_peg(x)

    draw_stack(a, PEG_X[0])
    draw_stack(b, PEG_X[1])
    draw_stack(c, PEG_X[2])

    screen.update()


def draw_stack(stack: Stack, x):
    y = BASE_Y
    for disk in stack.stack:
        draw_disk(disk, x, y)
        y += DISC_HEIGHT


def draw_disk(disk: Disk, x, y):
    t = turtle.Turtle(visible=False)
    t.shape("square")
    t.penup()
    t.goto(x, y)
    t.shapesize(stretch_wid=1, stretch_len=disk.n * 1.2)
    t.color("black", "skyblue")
    t.stamp()


def animate_move(from_stack: Stack, to_stack: Stack):
    disk = from_stack.peek()
    if disk is None:
        return

    from_index = [a, b, c].index(from_stack)
    to_index = [a, b, c].index(to_stack)

    start_x = PEG_X[from_index]
    end_x = PEG_X[to_index]

    start_y = BASE_Y + (len(from_stack.stack) - 1) * DISC_HEIGHT
    end_y = BASE_Y + len(to_stack.stack) * DISC_HEIGHT

    t = turtle.Turtle()
    t.shape("square")
    t.shapesize(stretch_wid=1, stretch_len=disk.n * 1.2)
    t.color("black", "yellow")
    t.penup()
    t.goto(start_x, start_y)

    for _ in range(20):
        t.sety(t.ycor() + 10)
        screen.update()
        time.sleep(0.01)

    steps = 30
    dx = (end_x - start_x) / steps
    for _ in range(steps):
        t.setx(t.xcor() + dx)
        screen.update()
        time.sleep(0.01)

    while t.ycor() > end_y:
        t.sety(t.ycor() - 10)
        screen.update()
        time.sleep(0.01)

    t.hideturtle()


redraw_towers()
time.sleep(0.5)

print(f"A:{a}, B:{b}, C:{c}")
move(n, a, b, c)

turtle.done()
