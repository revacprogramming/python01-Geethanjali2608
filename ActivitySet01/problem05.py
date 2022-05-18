def computepay(hrs,rate):
    if hrs>40:
        pay=40*rate+(hrs-40)*rate*1.5
    else:
        pay=hrs*rate
    return pay
hrs=float(input("enter hours:"))
rate=float(input("enter rate:"))
pay=computepay(hrs,rate)
print(pay)

