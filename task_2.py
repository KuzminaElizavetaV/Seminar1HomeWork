''' задача 2. Напишите программу для проверки истинности утверждения:
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.'''
X = bool(input('Введите True (1) или False (0): '))
Y = bool(input('Введите True (1) или False (0): '))
Z = bool(input('Введите True (1) или False (0): '))
def is_True(X, Y, Z):
   return not (X or Y or Z) == (not X and not Y and not Z)
print(is_True(X, Y, Z))