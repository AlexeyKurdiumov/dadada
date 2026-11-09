class Node:
    def __init__(self, key=None, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right
def compare_trees(first, second):
    if first is None and second is None:
        return True
    elif first is None or second is None:
        return False
    elif (first.key == second.key and compare_trees(first.left, second.left)
          and compare_trees(first.right, second.right)):
        return True
    return False 
#proverka
x = Node(1)
x.left = Node(2)
x.right = Node(3)
x.left.left = Node(4)
x.left.right = None
x.right.left = Node(6)
x.right.right = Node(7)

y = Node(1)
y.left = Node(2)
y.right = Node(3)
y.left.left = Node(4)
y.left.right = Node(5)
y.right.left = Node(6)
y.right.right = Node(7)

z = Node(1)
z.left = Node(2)
z.right = Node(3)
z.left.left = Node(4)
z.left.right = Node(5)
z.right.left = Node(6)
z.right.right = Node(7)

print(compare_trees(x, y))
print(compare_trees(x, z))
print(compare_trees(y, z))