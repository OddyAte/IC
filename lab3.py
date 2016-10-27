import math

def sign(x):
    if x > 0:
        print("face parte din clasa 1\n")
    elif x < 0:
        print("face parte din clasa 2\n")

def neuron(neu):
    clasa = neu[0] + neu[1] + neu[2]
    sign(clasa)


x = [2,1,2]
y = [1,-1,4]

print("X:",x)
print("Y:",y)
print()
ps = x[0] * y[0] + x[1] * y[1] + x[2] * y[2]
print("Produsul scalar:",ps)

lux = math.sqrt(x[0]**2+x[1]**2+x[2]**2)
print("Lungimea vectorului X:",lux)

luy = math.sqrt(y[0]**2+y[1]**2+y[2]**2)
print("Lungimea vectorului Y:",luy)

print("Cosinusul unghiului dintre ei:",ps/lux*luy)
print()

p0 = [-1,-1,-1]
print("P0:",p0)
print("P0 ", end="")
neuron(p0)
p1 = [-1,-1,1]
print("P1:",p1)
print("P1 ", end="")
neuron(p1)
p2 = [-1,1,-1]
print("P2:",p2)
print("P2 ", end="")
neuron(p2)
p3 = [-1,1,1]
print("P3:",p3)
print("P3 ", end="")
neuron(p3)
p4 = [1,-1,1]
print("P4:",p4)
print("P4 ", end="")
neuron(p4)
p5 = [1,-1,1]
print("P5:",p5)
print("P5 ", end="")
neuron(p5)
p6 = [1,1,-1]
print("P6:",p6)
print("P6 ", end="")
neuron(p6)
p7 = [1,1,1]
print("P7:",p7)
print("P7 ", end="")
neuron(p7)


