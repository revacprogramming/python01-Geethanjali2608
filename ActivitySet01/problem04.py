'''hrs = float(input("Enter hours: "))
rate=float(input("enter rate:"))
if(hrs>40):
    pay=40*rate+(hrs-40)*1.5*rate
    print("pay:",pay)
else:
    pay=hrs*rate
    print("pay:",pay)'''

x=float(input("Enter score:"))
if x>=0.9:
    print("A")
elif x>=0.8 and x<0.9:
    print("B")
elif x>=0.7 and x<0.8:
    print("C")    
elif x>=0.6 and x<0.7:
    print("D")    
elif x<0.6:
    print("F")
else:
    print("invaid input")

    
