import random as rnd
import turtle as t

t.shape('turtle')
t.speed(0)
x = 0
while x < 1:
    t.forward(rnd.randint(0, 50))
    t.left(rnd.randint(-180, 180))
