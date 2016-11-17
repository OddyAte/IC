import math

def signum(y):
    if y < 0:
        return -1
    elif y > 0:
        return 1
    else:
        return 0

d1 = -1
d2 = 1
x1 = [2,1,-1]
x2 = [0,-1,-1]
iter = 1
c = 0.1
w1 = [0, 1, 0]
o1 = 0
o2 = 0
w = [0,0,0]
ww = [0,0,0]
w2 = [0,0,0]

while iter <= 10:
    print("Iteratie:",iter)

    for i in range(0,len(x1)):
        o1 = o1 + x1[i] * w1[i]
    for i in range(0,len(x1)):
        w1[i] = w1[i] + x1[i]*c*(d1-signum(o1))
        w[i] = w1[i]
    print("\to1:",o1)
    print("\tw1:",w)

    for i in range(0, len(x2)):
        o2 = o2 + x2[i]*w[i]
    for i in range(0,len(x2)):
        w2[i] = w[i] + x2[i]*c*(d2-signum(o2))
        ww[i] = w2[i]
    print("\to2:",o2)
    print("\tw2",ww)

    w1 = ww
    if ww == w:
        break

    w = [0,0,0]
    ww = [0,0,0]
    w2 = [0,0,0]
    o1 = 0
    o2 = 0
    iter += 1
    print("")