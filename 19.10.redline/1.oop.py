import math
import itertools
class Vector:
    def __init__(self, *args):
        if len(args) == 3:
            self.x, self.y, self.z = args
        else:
            raise ValueError("Неверное количество аргументов. Ожидается 3 числа или строка '(x, y, z)'")
      """операции с векторами""""  
    def __repr__(self):
        return f"Vector({self.x}, {self.y}, {self.z})"
    
    def __abs__(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y, self.z + other.z)
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y, self.z - other.z)
        return NotImplemented

    def __mul__(self, other):
        if isinstance(other, Vector):
            
            return self.x * other.x + self.y * other.y + self.z * other.z
        elif isinstance(other, (int, float)):
            
            return Vector(self.x * other, self.y * other, self.z * other)
        return NotImplemented

    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        if isinstance(other, (int, float)):
            return Vector(self.x / other, self.y / other, self.z / other)
        return NotImplemented

    def cross(self, other):
        return Vector(
            self.y * other.z - self.z * other.y,
            self.z * other.x - self.x * other.z,
            self.x * other.y - self.y * other.x
        )
def center_of_mass(points):
    """поиск координат цм"""
    if not points:
        return None
    total = Vector(0, 0, 0)
    for p in points:
        total = total + p
    return total / len(points)

def max_area_triangle(points):
    """треугольник наибольшей площади"""
    max_area = 0
    best_points = None
    
    for p1, p2, p3 in itertools.combinations(points, 3):
        v1 = p2 - p1
        v2 = p3 - p1
        area = 0.5 * abs(v1.cross(v2))
        if area > max_area:
            max_area = area
            best_points = (p1, p2, p3)
            
    return best_points, max_area
    
    
    
if __name__ == "__main__":
    v1 = Vector(1, 2, 3)
    v2 = Vector("(4, 5, 6)")
    print(f"v1: {v1}, v2: {v2}")
    print(f"Сложение: {v1 + v2}")
    print(f"Вычитание: {v2 - v1}")
    print(f"Скалярное произведение: {v1 * v2}")
    print(f"Умножение на число: {v1 * 2}")
    print(f"Модуль v1: {abs(v1):.4f}\n")
    
    
    
    points = [
        Vector(0, 0, 0),
        Vector(1, 0, 0),
        Vector(0, 1, 0),
        Vector(5, 5, 5),
        Vector(10, 10, 10)
    ]


    
    com = center_of_mass(points)
    print(f"Центр масс: {com}")


    
    best_triangle, max_area = max_area_triangle(points)
    print(f"Точки с наибольшей площадью: {best_triangle}")
    print(f"Площадь: {max_area:.2f}")