"""
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


a  = [ 12, 3, 7, 9, 6, 8, 4, 2, 0, 7]

print(max(a))

a = 6
for i in range(10):
    i+=1
    print(f'{a}X{i} = {a*i}')

ide = []
pesol = []
altural = []

entrada = 1
while(entrada == 1) :
    id = int(input('digite a matrícula da pessoa: '))
    if id == 0 : 
        entrada = 0
    else:
        peso = float(input('digite o peso da pessoa: '))
        altura = float(input('digite a altura da pessoa: '))
        ide.append(id)
        pesol.append(peso)
        altural.append(altura)
else:
    if len(pesol) > 0:
        print(f'mais gordo: {max(pesol)}, mais magro: {min(pesol)}')
    if len(altural) > 0:
        print(f'mais alto: {max(altural)}, mais baixo: {min(altural)}')
    print(f'media de peso: {sum(pesol)/len(pesol)}') if len(pesol) > 0 else print('lista de pesos vazia')
    print(f'media de altura: {sum(altural)/len(altural)}') if len(altural) > 0 else print('lista de alturas vazia')

times = "bucks", "raptors", "76ers", "celtics", "pacers", "nets", "magic", "pistons", "hornets", "heat"
print(times[:5])
print(times[6:])
print(times.index("celtics"))
print(sorted(times))

tupla = ()

for i in range(4):
    tupla += (int(input("entre com o novo elemento: ")), )

j = 0
for i in tupla:
    if i == 9:
        j+=1
print(f'quantidade de elementos iguais a 9: {j}')

for i in range(len(tupla)):
    if tupla[i] == 3:
        print(f'índice do primeiro número 3 na tupla: {i}')
        break
print('numeros pares na tupla: ')
for i in tupla:
    if i%2 == 0:
        print(i)

"""
text = input("entre com o texto: ")
dic = {'a': 0,
        'e': 0,
        'i': 0,
        'o': 0,
        'u': 0}
for i in text:
    if i == 'a':
        dic[i] +=1
    elif i == 'e':
        dic[i] +=1
    elif i == 'i':
        dic[i] +=1
    elif i == 'o':
        dic[i] +=1
    elif i == 'u':
        dic[i] +=1

print(dic)