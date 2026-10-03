a, b = input().split()
a = a[1::-1] + a[2:]
b = b[1::-1] + b[2:]
print(a,'-',b, sep="")