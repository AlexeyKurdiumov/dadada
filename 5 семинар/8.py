A = {3, 6, 9, 12, 15}
B = {2, 4, 6, 8, 10, 12}
print(*(A.difference(A.intersection(B))), *(B.difference(B.intersection(A))))
print(*(A^B))
print(*(A&B))