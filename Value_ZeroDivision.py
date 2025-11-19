while True:
    try:
        osztando = 10
        oszto = float(input(f"Mennyivel osszam a {osztando}-et?"))

        print(f"A hányados {osztando/oszto}")
        break
    except ZeroDivisionError as e:
        print(e)
        print("ZeroDivisionError: Nullával nem osztunk!")
    except ValueError as e:
        print(e)
        print("ValueError: Nem számot adtál meg!")