# 1

imie = "Rafał"
nazwisko = "Pęcak"
miasto = "Krakow"

wynik = "To jest " + imie + " " + nazwisko + ". Jego miejsce urodzenia to " + miasto
wynik1 = f"To jest {imie} {nazwisko}. Jego miejsce urodzenia to {miasto}"

print(wynik)
print(wynik1)

# 2

result = "to jest krótkie zdanie na temat Jana"

result_myslnik = result.replace(" ","-")

print(result_myslnik)

#3

greeting = "hello world"

greeting_dlugosc = greeting.__len__()
greeting_duza = greeting.upper()
greeting_duza_pierwsza = greeting.capitalize()

print(greeting_dlugosc)
print(greeting_duza)
print(greeting_duza_pierwsza)

#4

movie = "lord of the rings"

movie_tytul = movie.title()

print(movie_tytul)

#5

movie1 = "dzisiaj jest sobota"

movie1_piata = movie1[5]

print(movie1_piata)
