import math

def sign(x):
    if x > 0:
        print("face parte din clasa 1")
    elif x < 0:
        print("face parte din clasa 2")

def signum(y):
    if y < 0:
        return -1
    elif y > 0:
        return 1
    else:
        return 0

def neuron(neu):
    clasa = neu[0] + neu[1] + neu[2]
    out1 = neu[0]
    out2 = neu[1]
    out3 = neu[2]
    save1 = out1
    save2 = out2
    save3 = out3
    sign(clasa)
    out1 = signum(save2 - save3)
    out2 = signum(save1 - save3)
    out3 = signum(-save1 - save2)
    if out1 == save1 and out2 == save2 and out3 == save3:
        print("Iesire stabila")

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
print()

p1 = [-1,-1,1]
print("P1:",p1)
print("P1 ", end="")
neuron(p1)
print()

p2 = [-1,1,-1]
print("P2:",p2)
print("P2 ", end="")
neuron(p2)
print()

p3 = [-1,1,1]
print("P3:",p3)
print("P3 ", end="")
neuron(p3)
print()

p4 = [1,-1,1]
print("P4:",p4)
print("P4 ", end="")
neuron(p4)
print()

p5 = [1,-1,1]
print("P5:",p5)
print("P5 ", end="")
neuron(p5)
print()

p6 = [1,1,-1]
print("P6:",p6)
print("P6 ", end="")
neuron(p6)
print()

p7 = [1,1,1]
print("P7:",p7)
print("P7 ", end="")
neuron(p7)
print()


