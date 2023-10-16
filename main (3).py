# Високосный год 

def is_year_leap(year):
  if year % 4 == 0:
    return True
  else:
    return False

# Квадрат 
def square(n):
  p = n * 4
  s = n * n
  d = ((n**2)*2)**0.5
  res = (p, s, d)
  return res

# Времена года
seas = [[12, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11]]

def season(n):
  for i in range(4):
    for g in range(3):
      if n == seas[i][g]:
        if i == 0:
          return "Зима"
        elif i == 1:
          return "Весна"
        elif i == 2:
          return "Лето"
        else:
          return "Осень"

# Банковский вклад 
def bank(a, years):
  for i in range(years):
    a *= 1.1
  return a

# Простые числа
def is_prime(n):
  for i in range(2, n):
    if n % i == 0:
      return False
    else:
      return True

#Правильная дата
d31 = [1, 3, 5, 7, 8, 10, 12]
d30 = [4, 6, 9, 11]
def date(d, m, y):
  if d < 0 or m < 0:
    return False
  if m == 2:
    if d == 29 and y % 4 == 0:
      return True
    if d < 29:
      return True
    else:
      return False

  for i in d31:
    if m == i and d <= 31:
      return True

  for i in d30:
    if m == i and d <= 30:
      return True

  return False

day = int(input("Введите день: "))
month = int(input("Введите месяц(пример: 2): "))
year = int(input("Введите год(пример: 2007): "))

print(date(day, month, year))