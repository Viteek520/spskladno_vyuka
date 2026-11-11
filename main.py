with open("DNA.txt", "w") as soubor:
    soubor.write("ATGCAGTCTTCAG")
    soubor.write("ATGCATGCTTGAGC")
    soubor.write("To je Vse")

with open ("DNA.txt", "r") as s:
    for radek in s:
        index = radek.find("AGT")
        print(f"Písmena AGT za sebou byly nalezena na indexu: {index}")