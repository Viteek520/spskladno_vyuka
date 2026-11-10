konec = True
while konec:
    try:
        prvni_cislo = input("Zadejte první číslo (pokuď chcete skončit napište konec): ")
        if prvni_cislo == "konec":
            konec = False
        else:
            prvni_cislo = int(prvni_cislo)
            operace = input("Zadejte operaci (+,-,*,/): ")
            druhe_cislo = int(input("Zadejte druhé číslo: "))
        if operace == "+":
            vysledek = prvni_cislo + druhe_cislo
            print(vysledek)
        elif operace == "-":
            vysledek = prvni_cislo - druhe_cislo
            print(vysledek)
        elif operace == "*":
            vysledek = prvni_cislo * druhe_cislo
            print(vysledek)
        elif operace == "/":
            vysledek = prvni_cislo / druhe_cislo
            print(vysledek)
        else:
            print("Operace má špatný symbol")
    except ZeroDivisionError:
        print("Nelze dělit nulou.")
        

