'''Írj egy programot, ami a felhasználótól három egész számot számot kér be egyesével, ezeket eltárolja egy listában, majd a képernyőre kiírja a lista tartalmát! Ha a felhasználó nem számot ad meg, kapjon hibaüzenetet, és ismétlődjön meg a bekérés!
'''
while True:
    try:
        szamlista = []
        for i in range(1, 4):
            szamlista.append(int(input(f"Adj meg egy egész számot ({i}/3): ")))
        print("A lista tartalma:", szamlista)
        break
    except ValueError:
        print("Nem egész számot adtál meg vagy nem számot adtál meg! Próbáld újra.")