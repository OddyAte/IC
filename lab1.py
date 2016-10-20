import csv
import statistics

i=0
with open('iris.csv', newline='') as f:
    reader = csv.reader(f)
    for row in reader:

        if i == 10:
            print(row)
            a = float(row[1])
            b = float(row[2])
            c = float(row[3])
            d = float(row[4])
            maxim1 = float(max(row[1],row[2],row[3],row[4]))
            minim1 = float(min(row[1],row[2],row[3],row[4]))
            list1 = [a,b,c,d]
            tau1 = statistics.stdev(list1)
        elif i == 20:
            print(row)
            x = float(row[1])
            y = float(row[2])
            z = float(row[3])
            q = float(row[4])
            maxim2 = float(max(row[1],row[2],row[3],row[4]))
            minim2 = float(min(row[1],row[2],row[3],row[4]))
            list2 = [x,y,z,q]
            tau2 = statistics.stdev(list2)
            break
        i += 1
f.close()
print()

pr = a * x + b * y + c * z + d * q
print("Produsul scalar =",pr)

row[0] = a * x
row[1] = b * y
row[2] = c * z
row[3] = d * q
print("Produsul vectorial =",'[',row[0],row[1],row[2],row[3],']')

maxmin1 = maxim1 - minim1
row[0] = (a-minim1)/maxmin1
row[1] = (b-minim1)/maxmin1
row[2] = (c-minim1)/maxmin1
row[3] = (d-minim1)/maxmin1
print("Scalare1 = ",'[',row[0],row[1],row[2],row[3],']')

maxmin2 = maxim2 - minim2
row[0] = (x-minim2)/maxmin2
row[1] = (y-minim2)/maxmin2
row[2] = (z-minim2)/maxmin2
row[3] = (q-minim2)/maxmin2
print("Scalare2 = ",'[',row[0],row[1],row[2],row[3],']')

xmed1 = (a + b + c + d)/4
row[0] = (a-xmed1)/tau1
row[1] = (b-xmed1)/tau1
row[2] = (c-xmed1)/tau1
row[3] = (d-xmed1)/tau1

print("Normalizare1 =",'[',row[0],row[1],row[2],row[3],']')

xmed2 = (x + y + z + q)/4
row[0] = (x-xmed2)/tau2
row[1] = (y-xmed2)/tau2
row[2] = (z-xmed2)/tau2
row[3] = (q-xmed2)/tau2

print("Normalizare2 =",'[',row[0],row[1],row[2],row[3],']')





