from sklearn.naive_bayes import GaussianNB
import numpy as np
import csv
import collections
s=0
a = []
b = []
with open('good_vibes.csv','rb') as f:
    reader = csv.reader(f)
    for row in reader:      
        a.append(row[0])
	b.append(row[12])  

a.pop(0)
b.pop(0)

s=0
for i in b:
    b[s]=int(b[s])
    s=s+1
#print a
#k = dict(zip(a,b))
#print k
o=0
z=0

names1 = []
zero = []
names2 = []
one = []

t=0
i=0
j=0
m=a[0]

while t!=9635:
    m = a[0]
    #print m,a[0]
    while 1 & t!=9635:
        if a[0]!=m:
            break
        else:
	    t=t+1
	    if b[0]==1:
		names1.append(a[0])
	        one.append(1.0)
		a.pop(0)
		b.pop(0)
	    else:
		names2.append(a[0])
		zero.append(1.0)
		a.pop(0)
		b.pop(0)

d = {x:names1.count(x) for x in names1}
e = {x:names2.count(x) for x in names2}


#print group 
print len(d)
print len(e)
#m = {}
#m[a[0]]=b[0]
#print m


total1 = 0.0
total2 = 0.0
for key, value in d.items():
    total1 = total1+value
#print total
for key, value in e.items():
    total2 = total2+value

total = total1+total2

result = {}

for key, value1 in d.items():
    value2=0
    for key1, val in e.items():
        if key1 == key:
            value2 = val
	    break
    final = ((value1/total1)*(total1/total))/((value1+value2)/total)
    result[key] = final

print result
 
