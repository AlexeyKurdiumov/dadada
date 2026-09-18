def pm(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    i = 3
    while i * i <= n:
        while n % i == 0:
            a.append(i)
            n //= i
        i += 2
    if n > 1:
        a.append(n)
    return a
n = int(input())
print(pm(n))