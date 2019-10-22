seq = [1,2,4,3]
print(seq)
flag = False
i=0
while i<=(len(seq)-2) and flag==False:
  if(seq[i]>seq[i+1]):
    flag = True
  i+=1
print(not(flag))
