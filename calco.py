#calcoding
from turtle import*
bgcolor('black')
t = Turtle()
t.speed(30)
a =["violet","indigo","blue","green","yellow","orange","red","gold","black","pink","purple","light blue","light green"]


for i in range(40):
    k = i%13
    t.color(a[k])
    t.circle(120)
    t.left(10)
for r in range(4):
    t.fd(100)
    t.right(90)
t.write("Diya Vijay" , font = ("courier",90,"bold"))       #To woright
t.write("Diya Vijay" , font = ("courier",90,"bold"))       #To woright
m =["red"]

for l in range(40):
    x = l%1
    t.color(m[x])
    t.circle(120)
    t.right(10)

m =["blue"]

for l in range(40):
    x = l%1
    t.color(m[x])
    t.circle(120)
    t.right(10)
t.write("Welcome",font = ("coutier",34,"bold"))
m =["gold"]

for l in range(40):
    x = l%1
    t.color(m[x])
    t.circle(120)
    t.left(10)

m =["purple"]

for l in range(40):
    x = l%1
    t.color(m[x])
    t.circle(120)
    t.left(10)


m =["light green"]

for l in range(40):
    x = l%1
    t.color(m[x])
    t.circle(120)
    t.right(10)

m =["yellow"]

for l in range(40):
    x = l%1
    t.color(m[x])
    t.circle(120)
    t.right(10)

m =["orange"]

for l in range(40):
    x = l%1
    t.color(m[x])
    t.circle(120)
    t.right(10)
m =["indigo"]

for l in range(40):
    x = l%1
    t.color(m[x])
    t.circle(120)
    t.right(10)
