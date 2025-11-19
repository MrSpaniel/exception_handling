try:
    szam = int(input("Adj meg egy számot!"))
    print(f"A szám négyzete: {szam ** 2}")
except ValueError:
    print("Nem számot adtál meg!")