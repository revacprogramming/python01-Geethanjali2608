# Loops & Iterators

'''x=float(input("Enter score:"))
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
    print("invaid input")'''


'''while True:
    print("loop")
    line=input('>')
    if line=='done':
        break
    print(line)
print("program terminated")'''

'''while True:
    line = input('> ')
    print("loop")
    if line[0] == '#':
        continue
    if line == 'done':
        break
    print(line)
print('Done!')'''



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
