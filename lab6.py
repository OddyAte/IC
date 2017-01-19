import math

def distanta(x, w):
    dist = 0
    for i in range(0, 2):
        dis = x[i] - w[i]
        dist = dist + (dis * dis)
    return math.sqrt(dist)


def distmin(x, w1, w2, w3):
    a = min(distanta(x, w1), distanta(x, w2), distanta(x, w3))
    return a


def castigator(x, wc1, wc2, wc3):
    wcastig = []
    c = 0.5

    if distmin(x, wc1, wc2, wc3) == distanta(x, wc1):
        for i in range(0, 2):
            a = x[i] - wc1[i]
            b = wc1[i]
            d = (b + (c * a))

            wcastig += [d]
            wc1[i] = wcastig[i]


        print("\t\tw1:", end="")

    if distmin(x, wc1, wc2, wc3) == distanta(x, wc2):
        for i in range(0, 2):
            a = x[i] - wc2[i]
            b = wc2[i]
            d = (b + (c * a))

            wcastig += [d]
            wc2[i] = wcastig[i]

        print("\t\tw2:", end="")

    if distmin(x, wc1, wc2, wc3) == distanta(x, wc3):
        for i in range(0, 2):
            a = x[i] - wc3[i]
            b = wc3[i]
            d = (b + (c * a))

            wcastig += [d]
            wc3[i] = wcastig[i]

        print("\t\tw3:", end="")

    return wcastig


x1 = [45, 85]
x2 = [50, 43]
x3 = [40, 80]
x4 = [55, 42]
x5 = [200, 43]
x6 = [48, 40]
x7 = [195, 41]
x8 = [43, 87]
x9 = [190, 40]

w1 = [10, 50]
w2 = [50, 90]
w3 = [150, 10]

counter = 0

while counter < 20:
    counter += 1
    print("Iteratia", counter)
    print("x1:", x1, end="")
    print("\t", castigator(x1, w1, w2, w3))
    print("x2:", x2, end="")
    print("\t", castigator(x2, w1, w2, w3))
    print("x3:", x3, end="")
    print("\t", castigator(x3, w1, w2, w3))
    print("x4:", x4, end="")
    print("\t", castigator(x4, w1, w2, w3))
    print("x5:", x5, end="")
    print("\t", castigator(x5, w1, w2, w3))
    print("x6:", x6, end="")
    print("\t", castigator(x6, w1, w2, w3))
    print("x7:", x7, end="")
    print("\t", castigator(x7, w1, w2, w3))
    print("x8:", x8, end="")
    print("\t", castigator(x8, w1, w2, w3))
    print("x9:", x9, end="")
    print("\t", castigator(x9, w1, w2, w3))
    print("")
