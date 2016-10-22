import math

x = [2,1,2]
y = [1,-1,4]

print(x)
print(y)
ps = x[0] * y[0] + x[1] * y[1] + x[2] * y[2]
print("Produsul scalar:",ps)

lux = math.sqrt(x[0]**2+x[1]**2+x[2]**2)
print("Lungimea vectorului X:",lux)

luy = math.sqrt(y[0]**2+y[1]**2+y[2]**2)
print("Lungimea vectorului Y:",luy)

print("Cosinusul unghiului dintre ei:",ps/lux*luy)