import sys
a=int(sys.argv[1])
b=int(sys.argv[2])
def lcm(num1,num2):
 if num1%num2==0:
  print(f"The lcm is:{num1}")
 elif num2%num1==0:
  print(f"the lcm is:{num2}")
 else:
  print(f"Thr lcm is:{num1*num2}")
def gcd(num1,num2):
 if num1<num2:
  num1=num1+num2
  num2=num1-num2
  num1=num1-num2
 while num1%num2!=0:
  num2=num1%num2
 print(f"The gcd is:{num2}")
lcm(a,b)
gcd(a,b)
 