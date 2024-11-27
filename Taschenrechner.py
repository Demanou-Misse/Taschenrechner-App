#Tachenrechner-App: Addition, Subtraktion, Multiplikation, Division, Faktorielle
print(" 1: Addition, 2: Subtraktion, 3: Mutiplikation, 4: Division, 5: Faktorielle")
wahl = int(input(" Wählen Sie eine Operation: "))
if wahl == 5:
    f = int(input("Geben Sie eine Zahl ein: "))
    def faktorielle(f):
        if f == 1:
            return 1
        else:
            return f * faktorielle(f - 1)
    
    print(f"Ergebnis: {f}! = {faktorielle(f)}")
elif wahl <= 0 or wahl > 5:
    print(" Sie sollten zwischen [1...5] wählen")
else:
    a = float(input("Geben Sie eine Zahl ein: "))
    b = float(input("Geben Sie eine zweite Zahl ein: "))
    if wahl == 1:
        print(f"Ergebnis: {a} + {b} = {a + b}")
    elif wahl == 2:
        print(f"Ergebnis: {a} - {b} = {a - b}")
    elif wahl == 3:
        print(f"Ergebnis: {a} * {b} = {a * b}")
    elif wahl == 4:
        if b == 0:
            print("Fehler: Division durch 0 ist unmöglich")
        else:
            print(f"Ergebnis: {a} / {b} = {a / b}")
print("* Vielen Dank, dass Sie mein Projekt getestet haben *")
   


