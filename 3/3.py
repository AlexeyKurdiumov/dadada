def ae(a, b):
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        elif b > a:
            b = b % a
        else:
            return(a)
    return a + b
a = int(input())
b = int(input())
print(ae(a, b))