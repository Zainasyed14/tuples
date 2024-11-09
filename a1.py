weather=(1,0,0,0,1,1,0)
rainyDay=0
sunnyDay=0
for i in weather:
    if(i==1):
        rainyDay+=1
    else:
        sunnyDay+=1
if(rainyDay>sunnyDay):
    print("This week was rainy")
else:
    print("This week was sunny")
