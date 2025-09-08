p = float(input("Enter principal:"))
r = float(input("Enter rate of intrest(%):"))
t = float(input("Enter time(in year) :"))
si = p*t*r/100
print(" interest  =")
print(si)
#space


emi = (si+p)/(t*12)
print("EMI = " , emi)
print(emi) 