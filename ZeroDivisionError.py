try:
    osztando = 10
    oszto = float(input(f"Mennyivel osszam a {osztando}-ot?"))

    print(f"A hányados {osztando/oszto}")
except ZeroDivisionError:
    print("Nullával nem osztunk!")