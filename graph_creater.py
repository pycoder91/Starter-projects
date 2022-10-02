
from matplotlib import pyplot as pp
from matplotlib import style
style.use("ggplot")

a = []
b = []

c1 = 0
c2 = 0

noOfPlot = int(input("enter total number plot you want to create: "))

for i in range(noOfPlot):
    for j in range(1):
        x = eval(input(f"enter x{c1}: "))
        a.append(x)
        c1 += 1
        y = eval(input(f"enter y{c2}: "))
        b.append(y)
        c2 += 1

pp.plot(a, b)
pp.show()