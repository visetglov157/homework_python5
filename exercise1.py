def recApowB(a, b):
    if b == 0:
        return 1
    return a * recApowB(a, b - 1)

a = int(input('Введите A: '))
b = int(input('Введите B: '))
print(recApowB(a, b))