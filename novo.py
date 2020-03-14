import time
import datetime
a = 0
b = 0

print(a+b)
print(a-b)
print(a*b)
if(b != 0):
    print(a/b)
elif a!=0:
    print(b/a)
else:
    print('os dois são nulos')

now = datetime.datetime.now()
inicio = now.replace(hour=19, minute=0, second=0, microsecond=0)
fim = now.replace(hour=6, minute=0, second=0, microsecond=0)
print(inicio<now<fim)

a = 13
b = 12

print(a if a>b else b)

x = 13
print("par" if x%2 == 0 else "impar")
print("negativo" if x<0 else "positivo")

carne = 1
kg = 5.2
total = 0
tipoPag = 1
if carne ==1:
    if kg >= 5:
        total += 4.9*kg
        print(f'filé duplo ----------- {kg} kilos ---------- R$ {4.9*kg:.2f}')
    else:
        total += 5.8*kg
        print(f'filé duplo ----------- {kg} kilos ---------- R$ {5.8*kg:.2f}')
elif carne == 2:
    if kg >= 5:
        total += 5.9*kg
        print(f'alcatra ----------- {kg} kilos ---------- R$ {5.9*kg:.2f}')
    else:
        total += 6.8*kg
        print(f'alcatra ----------- {kg} kilos ---------- R$ {6.8*kg:.2f}')
elif carne == 3:
    if kg >= 5:
        total+=6.9*kg
        print(f'picanha----------- {kg} kilos ---------- R$ {6.9*kg:.2f}')
    else:
        total+=7.8*kg
        print(f'picanha ----------- {kg} kilos ---------- R$ {7.8*kg:.2f}')
if tipoPag == 1:
    total -= 0.05*total
print(f'total: {total:.2f}')