import random
x = random.randint(1,100)

while True:
    y = int(input("Podaj liczbę: "))
    if y > x:
        print("Podana liczba jest za duża")
    elif y < x:
        print("Podana liczba jest za mała")
    else:
        print("Podana liczba jest identyczna")
        break
print("Gra zakończona")