a = float(input("Введите a: "))
b = float(input("Введите b: "))
c = float(input("Введите c: "))
d = b * b - 4 * a * c
if a == 0 and b == 0:
    print(str(c) + " = 0, получается?")
elif a == 0:
    print("x = " + str(-c/b))
else:
    print("x1: " + str((-b + d ** (1 / 2)) / (2 * a)))
    print("x2: " + str((-b - d ** (1 / 2)) / (2 * a)))
input()

    
