a=int(input())
b=int(input())
c=int(input())
d=int(input())
e=int(input())
t=a+b+c+d+e
p=(t/500)*100
#print(p)
if(p>75):
    print("grade A")
elif(60<=p<74):
    print("grade B")
elif(35<=p<59):
    print("grade C")
elif(p<35):
    print("fail")    
else:
    print("invalid")            