def signum(y):
    if y < 0:
        return -1
    elif y > 0:
        return 1
    else:
        return 0


x1 = [1, -2]
x2 = [0, 1]
x3 = [2, 3]
x4 = [1, -1]
c = 1
iteratie = 1

print("x1:", x1)
print("x2:", x2)
print("x3:", x3)
print("x4:", x4)

wpas0 = [1, -1]
wpas1 = []
wpas2 = []
wpas3 = []
wpas4 = []

print("\nw :", wpas0)

while iteratie <= 3:
    # Pas1

    o1 = 0
    countx1 = 0
    print("\nIteratie :", iteratie)
    print("\tPasul 1:\t",end="")
    for i in range(0, len(x1)):
        o1 = o1 + x1[i] * wpas0[i]

    for i in range(0, len(x1)):
        countx1 += 1
        w1 = wpas0[i] + x1[i] * c * signum(o1)
        wpas1 += [w1]

    print("w':   ", wpas1)
    w1 = 0

    # Pas2

    o2 = 0
    countx2 = 0
    print("\tPasul 2:\t",end="")
    for i in range(0, len(x2)):
        o2 += x2[i] * wpas1[i]

    for i in range(0, len(x2)):
        countx2 += 1
        w2 = wpas1[i] + x2[i] * c * signum(o2)
        wpas2 += [w2]

    print("w'':  ", wpas2)
    w2 = 0

    #Pas3

    o3 = 0
    countx3 = 0
    print("\tPasul 3:\t",end="")
    for i in range(0, len(x3)):
        o3 += x3[i] * wpas2[i]

    for i in range(0, len(x3)):
        countx3 += 1
        w3 = wpas2[i] + x3[i] * c * signum(o3)
        wpas3 += [w3]

    print("w''': ", wpas3)
    w3 = 0

    #Pas4

    o4 = 0
    countx4 = 0
    print("\tPasul 4:\t",end="")
    for i in range(0, len(x4)):
        o4 += x4[i] * wpas3[i]

    for i in range(0, len(x4)):
        countx4 += 1
        w4 = wpas3[i] + x4[i] * c * signum(o4)
        wpas4 += [w4]

    print("w'''':", wpas4)
    w4 = 0

    iteratie +=1
    wpas0 = wpas4
    wpas1 = []
    wpas2 = []
    wpas3 = []
    wpas4 = []
