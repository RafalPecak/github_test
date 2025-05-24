# from datetime import datetime
#
# # 1
# from time import daylight
# from turtledemo.sorting_animate import start_ssort
#
# user_role = "klient"
# is_logged = "yes"
#
# if is_logged == "yes" and user_role == "admin":
#     print("Witaj w panelu admina")
# elif is_logged == "yes" and user_role == "mod":
#     print("Witaj  w panelu moderatora")
# elif is_logged == "yes" and user_role == "konto":
#     print("Witaj w panelu użytkownika")
# else:
#     print("Błąd logowania")
#
# # 2
# user_country = "Niemcy"
# country_list = ["Polska", "Niemcy", "Czechy"]
# if user_country in country_list :
#     print("Zamówienie z " + user_country)
# else:
#     print("Dostawa towaru niemożliwa")
#
#
# # 3
# current_date = datetime.now()
# current_time = current_date.hour
#
# if current_time >= 6 and current_time < 12:
#     print("Good Morning")
# elif current_time >= 12 and current_time < 18:
#     print("Good Afternoon")
# else:
#     print("Good Evening")
from ipaddress import summarize_address_range

# 1
# language = "Python"
#
# match language:
#     case "Python" | "PHP" | "Java":
#         print("Backend")
#     case "JavaScript" | "HTML":
#         print("Frontend")
#     case _:
#         print("Błędna wartość")
#
# # 2
# import datetime
#
# date = datetime.datetime.now()
# month = date.month
# match month:
#     case  1:
#         print("Styczeń")
#     case  2:
#         print("Luty")
#     case  3:
#         print("Marzec")
#     case  4:
#         print("Kwiecień")
#     case  5:
#         print("Maj")
#     case  6:
#         print("Czerwiec")

dictionary = dict(name="Rafał",lastname="Pęcak", age=50)
new_key = input("Jaki klucz chcesz znaleźć? ")

try:
    print(dictionary[new_key])
except KeyError:
    print("Podany klucz nie istnieje")


