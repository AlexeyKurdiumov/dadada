a = int(input())
b = str(input())
def draw_triangle(a, b):
    c= (a+1)//2
    if a % 2 == 1:
      for i in range(1, c+1):
          if i != 0:
              print(i* b)
      for i in range(1, c+1):
          print((c-i)* b)
    else:
        c = (a) // 2
        for i in range(1, c + 1):
            if i != 0:
                print(i * b)
        for i in range(1, c + 1):
            print((c + 1 - i) * b)
draw_triangle(a, b)