#задача Ряд-1
A = int(input())
B = int(input())

for i in range(A, B + 1):
  print(i)

#задача Ряд-2

A = int(input())
B = int(input())

e = 1

if B < A:
  e = -1
  B -= 2

for i in range(A, B + 1, e):
  print(i)

#Задача «Сумма N чисел»
N = int(input())
k = 0

for i in range(0, N):
  g = int(input())
  k += g
print(k)

#Задача «Факториал»
n = int(input())
a = 1

for i in range(2, n + 1):
  a *= i
print(a)

#Задача «Лесенка»
n = int(input())

for i in range(1, n+2):
  print(*[g for g in range(1, i)], sep='')

#Задача «Список квадратов»
N = int(input())

for i in range(1, N + 1):
  print(i ** 2)

#Задача «Степень двойки»
N = int(input())
e = 1

def delitna2(g):
  global e
  e = 1
  while True:
    if g % 2 == 1:
      return 0
      break
    if g == 2:
      return 1
      break
    else:
      g /= 2
      e += 1

for i in range(N, 2, -1):
  if i % 2 == 0:
    a = delitna2(i)
    if a == 1:
      print(i, e)
      break

# Задача «Утренняя пробежка»
x = int(input())
y = int(input())
a = float(x)
e = 1

while True:
  r = a * 0.1
  if a < y:
    a += r
    e += 1
  else:
    print(e)
    break

# Задача «Длина последовательности»
g = 0
while True:
  a = int(input())
  
  if a == 0:
    print(g)
    break
  else:
    g += 1

# Задача «Количество элементов, которые больше предыдущего»
c = 0
b = 0
while True:
  a = int(input())
  if b == 0:
    b = a
  if a > b:
    c += 1
  if a == 0:
    print(c)
    break
  b = a

# Задача «Числа Фибоначчи»
f = [0, 1]

a = int(input())

for n in range(2, a):
  if n < a:
    f.append((f[n-1] + f[n-2]))
else:
  print(f[a - 1])

#Задача «Максимальное число идущих подряд равных элементов»

b = 0
c = 1
d = 1
y = 0

while True:
  a = int(input())
  if a == 0:
    if y == 0:
      print(d)
    else:
      print(c)
    break
  if a == b and y == 0:
    c += 1
  if a != b and y == 0:
    y += 1
  if a == b and y == 1:
    d += 1
  if a != b and y == 1:
    if c >= d:
      d = 1
    else:
      c = 1
      y = 0
  
  b = a

#Задача «Четные индексы»
a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

for i in range(0, len(a)):
  if i % 2 == 0:
    print(a[i])

# Задача «Больше предыдущего»
a = [5, 4, 6, 9, 25, 1, 54, 3, 4]

for i in range(1, len(a)):
  if a[i] > a[i - 1]:
    print(a[i])

# Задача «Наибольший элемент»
a = [5, 4, 6, 9, 25, 1, 54, 39, 4]
index = 0
maxel = 0

for i in range(1, len(a)):
  if maxel < a[i]:
    index = i
    maxel = a[i]
print(maxel, index)

# Задача «Шеренга»
a = [190, 187, 185, 185, 182, 179, 161]

X = int(input())

if X > a[0]:
  print(1)
else:
  for i in range(0, len(a)):
    if X <= a[-1]:
      print(len(a) + 1)
      break
    else:
      if X <= a[i] and X > a[i + 1]:
        print(i + 2)

# Задача «Переставить соседние»
a = [13, 45, 41, 2, 56, 34, 1]
secondpar = len(a)
z = 0

if len(a) % 2 == 1:
  secondpar = len(a) - 1

for i in range(0, secondpar, 2):
  z = a[i]
  a[i] = a[i + 1]
  a[i + 1] = z
print(a)

# Задача «Переставить min и max»
a = [2, 45, 41, 25, 56, 34, 15]
minel = 0
maxel = 0
z = 0

for i in range(1, len(a)):
  if a[minel] > a[i]:
    minel = i
  if a[maxel] < a[i]:
    maxel = i
else:
  z = a[minel]
  a[minel] = a[maxel]
  a[maxel] = z
  print(a)

#Задача «Удалить элемент»
a = [2, 45, 41, 25, 56, 34, 15]
k = int(input())
z = a[k]

if k == len(a) - 1:
  a.pop()
  print(a)

else:
  for i in range(k + 1, len(a)):
    a[k] = a[i]
  else:
    a[-1] = z
    a.pop()
    print(a)

#Задача «Вставить элемент»
a = [2, 45, 41, 25, 56, 34, 15]
k = int(input())
C = int(input())

a.append(C)

for i in range(len(a) - 1, -1, -1):
  if k < i:
    a[i] = a[i - 1]
    a[i - 1] = C
  else:
    print(a)
    break 

#Задача «Ферзи»
n = 8
x = []
y = []
for i in range(n):
    nx, ny = [int(s) for s in input().split()]
    x.append(nx)
    y.append(ny)

bl = True
for i in range(n):
    for k in range(i + 1, n):
        if x[i] == x[k] or y[i] == y[k] or abs(x[i] - x[k]) == abs(y[i] - y[k]):
            bl = False

if bl == False:
    print('NO')
else:
    print('YES')
