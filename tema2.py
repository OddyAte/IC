def distanta(x, c):
    dist = 0
    a = abs(x[0] - c[0])
    b = abs(x[1] - c[1])
    dist = a + b
    dist = float("%.2f" % dist)
    return dist

def distantamin(x, c1, c2, c3):
    a = min(distanta(x, c1), distanta(x, c2), distanta(x, c3))
    return a

x1 = [45, 85]
x2 = [50, 43]
x3 = [40, 80]
x4 = [55, 42]
x5 = [200, 43]
x6 = [48, 40]
x7 = [195, 41]
x8 = [43, 87]
x9 = [190, 40]

lista = [x1,x2,x3,x4,x5,x6,x7,x8,x9]

p1 = [40, 45]
p2 = [40, 90]
p3 = [210, 50]

counter = 1

while (counter < 10):
    print("Iteratia numarul", counter)
    print("Centroizi:",p1,",",p2,",",p3)
    print("\t\t\t    Distanta1" + "\t\tDistanta2" + "\t    Distanta3" + "\t\tCluster")

    count1 = 0
    count2 = 0
    count3 = 0

    c1 = [0, 0]
    c2 = [0, 0]
    c3 = [0, 0]

    count = 1
    x = [0, 0]

    for i in range (0,9):
        x = lista[i]

        print("x", x, "|  \t", distanta(x, p1), "  \t|  \t", distanta(x, p2), "  \t|\t", distanta(x, p3), "\t  |\t  ",
              end="")
        if distantamin(x, p1, p2, p3) == distanta(x, p1):
            print("1")
            for i in range(0, 2):
                c1[i] += x[i]
            count1 += 1
        if distantamin(x, p1, p2, p3) == distanta(x, p2):
            print("2")
            for i in range(0, 2):
                c2[i] += x[i]
            count2 += 1
        if distantamin(x, p1, p2, p3) == distanta(x, p3):
            print("\t  3")
            for i in range(0, 2):
                c3[i] += x[i]
            count3 += 1
    for i in range(0, 2):
        c1[i] /= count1
        c1[i] = float("%.2f" % c1[i])
        c2[i] /= count2
        c2[i] = float("%.2f" % c2[i])
        c3[i] /= count3
        c3[i] = float("%.2f" % c3[i])

    print("Centroid 1:", c1)
    print("Centroid 2:", c2)
    print("Centroid 3:", c3)
    print()

    if p1[0] == c1[0] and p1[1] == c1[1] and p2[0] == c2[0] and p2[1] == c2[1] and p3[0] == c3[0] and p3[1] == c3[1]:
        break

    for i in range(0,2):
        p1[i] = c1[i]
        p2[i] = c2[i]
        p3[i] = c3[i]

    counter += 1
