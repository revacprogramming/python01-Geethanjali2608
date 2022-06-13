# Files

#filename = "dataset/mbox-short.txt"

fname=input("enter file name:")
fhand = open(fname,'r')
count = 0
total=0
for line in fhand:
    if not line.startswith('X-DSPAM-Confidence:'):
      continue
    p=line.find('0')
    num=line[p:]
    c=float(num)
    total=total+c
    count=count+1
print("Average spam confidence:",total/count)

