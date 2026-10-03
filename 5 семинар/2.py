import math
r, a = map(int, input().split())
length = 2 * math.pi * r
Sq1 = math.pi * r**2
Sq2 = a**2
print(f"""Длина окружности равно {length:.2f}.
       Площадь круга составляет {100 * (Sq1/Sq2):.2f}% от площади квадрата""")