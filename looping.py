x=0
y=0
i=0
a=[1,2,3,4,5]
b=[1,2,3,4,5,6]
while i<len(a) and a[i]>0:
  y+=1
  for j in range(i,len(b)):
    x+=1
    print("mid"+str(x))
    print(y)
  i+=1
print("end"+str(x))
