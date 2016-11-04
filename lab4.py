xn = 1000
c = 0.1

x = xn - c * (12 * xn - 12)

while abs(x - xn) > 0.0001:
    xn = x
    x = xn - c * (12 * xn - 12)
    xprint = 6 * (x * x) - 12 * x + 1
    print("f(x)=", xprint)

print()

gx = 100
gy = 100
gxy = 1

while abs(gxy - gx) > 0.0001 and abs(gxy-gy)>0.0001:
    gxd = gx - c * (2 * gx)
    gyd = gy - c * (4 * gy)
    gx = gxd
    gy = gyd
    gxy = gx * gx + 2 * (gy * gy)
    print("g(x) = ", gx)
    print("g(y) = ", gy)
    print("g(x,y)=", gxy)

print()

hx = 200
hy = 200
hxy = 0.01

while abs(hxy - hx) > 0.0001 and abs(hxy - hy) > 0.0001:
    hxd = hx - c * (202 * hx - 200 * (hy * hy) - 2)
    hyd = hy - c * (-400 * hy * (hx - hy * hy))
    hx = hxd
    hy = hyd
    hxy = (1-hx) * (1 - hx) + 100 * ((hx - hy * hy ) * (hx - hy * hy))
    print("h(x)=",hx)
    print("h(y)=",hy)
    print("h(x,y)=",hxy)
