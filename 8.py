import sys
a=int(sys.argv[1])
b=int(sys.argv[2])
print(f"a:{a} b:{b}")
a=a+b
b=a-b
a=a-b
print(f"after swap a:{a} b:{b}")
