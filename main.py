# Задача №26
def degree(A,B):
    if B == 1:
        return A
    else:
        return A * degree(A, B-1)

print(degree(A=int(input('Введите целое число: ')),
             B=int(input('Введите целое число: '))))

# Задача №28
def sumNum(a, b):
    if b == 0:
        return a
    else:
        return sumNum(a+1, b-1)
print(sumNum(a=int(input('Введите целое число: ')),
             b=int(input('Введите целое число: '))))
