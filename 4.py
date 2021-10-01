import turtle as t

t.shape('circle')
t.speed(100)
x = -300
y = 0
dt = 0.1
Vx = 25
Vy = 50
i = 0
t.penup()
t.goto(-300, 0)
t.pendown()
while i < 1000:
    ay = -10 - 0.05 * Vy
    x += Vx * dt
    y += Vy * dt
    Vy += ay * dt
    ax = -0.05 * Vx
    Vx += ax * dt
    i += 1
    if y < 0:
        Vy = -Vy
    t.goto(x, y)
