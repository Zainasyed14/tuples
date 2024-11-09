a = (1,2,4,5,2,1)
b = len(a)-1
c = 0
flag=True
while(c<b):
 if(a[c]!=a[b]):
  flag=False
  break
 c = c+1
 b = b-1
if(flag==True):
 print("It is palindrome")
else:
 print("It is not palindrome")
