import turtle
import random

# 设置窗口
screen = turtle.Screen()
screen.bgcolor("white")
screen.title("彩色螺旋花")

# 创建turtle对象
t = turtle.Turtle()
t.speed(0)  # 最快速度
t.pensize(2)

# 定义一些颜色
colors = ["red", "yellow", "blue", "green", "purple", "orange"]


# 画花瓣的函数
def draw_flower(size):
    for _ in range(36):  # 画36片花瓣
        # 随机选择颜色
        t.color(random.choice(colors))

        # 画一片花瓣
        for _ in range(4):
            t.forward(size)
            t.right(90)

        t.right(10)  # 旋转一定角度开始画下一片花瓣
        size = size * 0.95  # 每次稍微缩小一点


# 开始绘画
t.penup()
t.goto(0, -100)  # 移动到起始位置
t.pendown()

# 画主花朵
draw_flower(200)

# 画茎
t.penup()
t.goto(0, -100)
t.setheading(270)  # 朝下
t.color("green")
t.pendown()
t.forward(200)


# 画叶子
def draw_leaf():
    t.color("green")
    t.begin_fill()
    for _ in range(30):
        t.forward(5)
        t.right(6)
    for _ in range(30):
        t.forward(5)
        t.right(6)
    t.end_fill()


# 画左边的叶子
t.penup()
t.goto(0, -200)
t.setheading(45)
t.pendown()
draw_leaf()

# 画右边的叶子
t.penup()
t.goto(0, -160)
t.setheading(315)
t.pendown()
draw_leaf()

# 隐藏海龟
t.hideturtle()

# 保持窗口打开
screen.mainloop()