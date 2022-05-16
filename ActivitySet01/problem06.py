# Loops & Iterators

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

friends = ['Joseph', 'Glenn', 'Sally']
for a in friends:
    print('Happy New Year:', a)
print('Done!')


