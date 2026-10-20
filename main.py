n = int(input("zadejte cislo: "))

for prvocislo in range (2, n):
    for delitel in range(2, n):
        if prvocislo % delitel != 0:
            continue
        else:
            pass