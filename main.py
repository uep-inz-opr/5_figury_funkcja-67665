class Kolo:
    suma1 = 0

    def __init__(self, promien):
        self.promien = promien

    def polekola(self):
        pole1 = round(math.pi * self.promien ** 2, 2)
        self.suma1 = self.suma1 + pole1


class Prostokat:
    suma2 = 0

    def __init__(self, dlugosc, szerokosc):
        self.dlugosc = dlugosc
        self.szerokosc = szerokosc

    def poleprostokata(self):
        pole2 = round(self.dlugosc * self.szerokosc, 2)
        self.suma2 = self.suma2 + pole2


class Trojkat:
    suma3 = 0

    def __init__(self, ramie1, ramie2, ramie3):
        self.ramie1 = ramie1
        self.ramie2 = ramie2
        self.ramie3 = ramie3

    def poletrojkata(self):
        p = (self.ramie1 + self.ramie2 + self.ramie3) / 2
        pole3 = round(math.sqrt((p * (p - self.ramie1) * (p - self.ramie2) * (p - self.ramie3))), 2)
        self.suma3 = self.suma3 + pole3


iloscfigur = float(input())
listafigur = []
a = 0
b = 0
c = 0
for i in range(int(iloscfigur)):
    figura = input().split()
    if len(figura) == 1:
        ilosc1 = Kolo(float(figura[0]))
        ilosc1.polekola()
        a = round(a + ilosc1.suma1, 2)
    if len(figura) == 2:
        ilosc2 = Prostokat(float(figura[0]), float(figura[1]))
        ilosc2.poleprostokata()
        b = round(b + ilosc2.suma2, 2)

    if len(figura) == 3:
        ilosc3 = Trojkat(float(figura[0]), float(figura[1]), float(figura[2]))
        ilosc3.poletrojkata()
        c = round(c + ilosc3.suma3, 2)

suma = round((a + b + c), 2)
print(suma)
