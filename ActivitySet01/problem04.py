hrs = float(input("Enter hours: "))
rate=float(input("enter rate:"))
if(hrs>40):
    pay=40*rate+(hrs-40)*1.5*rate
    print("pay:",pay)
else:
    pay=hrs*rate
    print("pay:",pay)

    
