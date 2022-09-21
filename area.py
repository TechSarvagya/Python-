class shape:
 def __init__(self,fillcolor):
  self.fillcolor=fillcolor
 def out(self):
  print("it is a 2-d shape")
class circle(shape):
 def __init__(self,rad):
  self.rad=rad
 def param(self):
  print("The parameter is:"+str(2*3.14*self.rad))
 def area(self):
  print("the area is:"+str(3.14*self.rad*self.rad))
class rectangle(shape):
 def __init__(self,l,b):
  self.l=int(l)
  self.b=int(b)
 def param(self):
  print("the parameter is:"+str(2*(self.l+self.b)))
 def area(self):
  print("The area is:"+str(self.l*self.b))

leng=input("enter length:")
bre=input("enter breadth:")

r=rectangle(leng,bre)
r.out()
r.param()
r.area()

  
