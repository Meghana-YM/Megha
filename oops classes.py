'''class cse:
    def fun():
        print("this is function")
o=cse() #object
cse.fun() #calling method'''
'''class cse:
    def fun(self):
        print("function")
o=cse()
cse.fun(o) '''
'''class cse:
    def __init__(self,name,rollno) -> None:
        #print(name,rollno)
        self.n=name
        self.rn=rollno
    def fun(s):
        print(s.n,s.rn)
s1=cse('dee',32)
s2=cse('chandu',36) 
s1.fun()
s2.fun()
print(s1.n,s2.n) '''  
'''import math               
class circle:
    def __init__(self,radius):
         self.r=radius
    def printing(self):
        print(math.pi*self.r*self.r)    
        pass
class rectangle:
    def __init__(self,l,b):
        self.l=l
        self.b=b
    def printing(self):
        print(self.l*self.b)
        pass
l=float(input())
b=float(input())
r=float(input())
o=circle(r)
o1=rectangle(l,b)
o.printing()
o1.printing()
o.area'''
#define a class royal enfield and have constructor take values for model 
class re:
    def __init__(self,name,color,mileage):
        self.name=name
        self.cl=color
        self.m=mileage 
a=re("classic 350",'black',10)
b=re('reo','red',30)
c=('himalayan','red',25) 
print(a.name,a.cl,a.m)
print(b.name,b.cl,b.m)
print(c.name,)                 

     