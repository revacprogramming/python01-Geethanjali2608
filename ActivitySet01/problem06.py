# Loops & Iterators

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

'''friends = ['Joseph', 'Glenn', 'Sally']
for a in friends:
    print('Happy New Year:', a)
print('Done!')'''


