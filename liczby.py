import math


# 1
a=5
b=7
result =  (a+b)*7
print(result)

# 2
c = [5,8,2]
max_num = max(c)
print(max_num)

# 3
f = 5
g = 8
h = 3
avg_num = round((f+g+h)/3,2)
print(avg_num)

# 4
temp = 301.23
celsius = temp - 273.15
print(celsius)

# 5
num = 25
pierwiastek = math.sqrt(num)
print(pierwiastek)

# 6
liczba = input("podaj liczbe: ")
liczba_int = int(liczba)
from datetime import datetime
czas = datetime.now()
print(czas.hour*liczba_int)
