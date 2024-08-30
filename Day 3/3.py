a, b, c = 1, 5, 4

delta = b ** 2 - 4 * a * c 
root1 = (-b - delta ** (1 / 2)) / (2 * a)
root2 = (-b + delta ** (1 / 2)) / (2 * a)

print('x1 =', root1)
print('x2 =', root2)