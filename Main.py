"""
Modul für die Simulation von Logikgattern
"""
import pymysql

class Logikgatter:
    def __init__(self):
        self.eingangA = False
        self.eingangB = False
        self. ausgang = False

    def ausgabe(self):
        print(self.ausgang)

    def setze_eingangA(self, neuer_wert):
        self.eingangA = neuer_wert

    def setze_eingangB(self, neuer_wert):
        self.eingangB = neuer_wert


# UNDGatter erbt von Logikgatter
# Methoden und Attribute werden übernommen
class UNDGatter(Logikgatter):
    """Das UndGatter ist ein Logikgatter, dass zu
    True auswertet, wenn beide Eingänge True sind.

    So könnte ihre Anwendung aussehen.

    >>> u = UNDGatter()
    >>> u.setze_eingangA(True)
    >>> u.eingangA
    True
    >>> u.setze_eingangB(False)
    >>> u.pruefe_zustand()
    >>> u.ausgang
    False

    """

    def __init__(self):
        self.eingangA = False
        self.eingangB = False
        self.ausgang = False

    def pruefe_zustand(self):
        """Die Methode überprüft die Eingänge auf ihren
        Wert und setzt den Ausgang auf True, wenn
        beide Eingänge true sind."""

        if self.eingangA == True and self.eingangB == True:
            self.ausgang = True
        else:
            self.ausgang = False


#1 Methoden der Klasse haben immer einen
# Parameter self. Die Methode __init__
# wird beim erzeugen von Objekten
# aufgerufen

#Main = UNDGatter()
#Main.setze_eingangA(True)
#Main.setze_eingangB(True)
#Main.pruefe_zustand()
#Main.ausgabe()


def gatterAusgeben(Logikgatter):
    for e1 in [False, True]:
        for e2 in [False, True]:
            Logikgatter.setze_eingangA(e1)
            Logikgatter.setze_eingangB(e2)
            Logikgatter.pruefe_zustand()
            print("eingangA:", e1, "eingangB:", e2)
            Logikgatter.ausgabe()


print("Teste alle möglichen Eingänge für das UND Gatter...")
ANDGate = UNDGatter()
gatterAusgeben(ANDGate)

class XORGatter(Logikgatter):
        """Das XorGatter ist ein Logikgatter, dass zu
        True auswertet, wenn ein Eingang True ist und einer False."""
        def __init__(self):
            """Die Initmethode initialisiert zwei Eingänge
            die jeweils True sind und einen Ausgang mit False."""
            self.eingangA = True
            self.eingangB = True
            self.ausgang = False

        def pruefe_zustand(self):
            """Die Methode überprüft die Eingänge auf ihren
            Wert und setzt den Ausgang auf True, wenn
            ein Eingang true ist und einer False."""
            if self.eingangA == True and self.eingangB == False or self.eingangA == False and self.eingangB == True:
                self. ausgang = True

            else:
                self.ausgang = False


print("Teste alle möglichen Eingänge für das XOR Gatter...")
xorGatter = XORGatter()
gatterAusgeben(xorGatter)

class ORGatter(Logikgatter):
    """Das ORGatter ist ein Logikgatter, dass zu
    False auswertet, wenn beide Eingang False sind."""
    def __init__(self):
        """Die Initmethode initialissiert zwei Eingänge
        die jeweils False sind und einen Ausgang mit False."""
        self.eingangA = False
        self.eingangB = False
        self.ausgang = False

    def pruefe_zustand(self):
        if self.eingangA == False and self.eingangB == False:
            self.ausgang= False
        else:
            self.ausgang= True

print("Teste alle möglichen Eingänge für das OR Gatter...")
orGatter = ORGatter()
gatterAusgeben(orGatter)

class NichtGatter(Logikgatter):

    def __init__(self):  # 1
        self.eingangA = False
        self.ausgang = True

    def pruefe_zustand(self):  # 1
        if self.eingangA == False:
            self.ausgang = True
        else:
            self.ausgang = False


print("Teste alle möglichen Eingänge für das Nicht Gatter...")
nichtGatter = NichtGatter()
gatterAusgeben(nichtGatter)

class XNORGatter(Logikgatter):

    def __init__(self):  # 1
        self.eingangA = False
        self.eingangB = False
        self.ausgang = True

    def pruefe_zustand(self):
        if self.eingangA == self.eingangB:
            self.ausgang = True
        else:
            self.ausgang = False

print("Teste alle möglichen Eingänge für das XNOR Gatter...")
xnorGatter  = XNORGatter()
gatterAusgeben(xnorGatter)


"""class NANDGatter(Logikgatter):
    def __init__(self):  # 1
        self.eingangA = False
        self.eingangB = False
        self.ausgang = True

    def pruefe_zustand(self):
        if self.eingangA == True and self.eingangB == True:
            self.ausgang = False
        else:
            self.ausgang = True

print("Teste alle möglichen Eingänge für das NANDGatter...")
nandGatter = NANDGatter()
gatterAusgeben(nandGatter)
"""

class NichtUndGatter(Logikgatter):
    def __init__(self):
        self.und_gatter = UNDGatter()
        self.nicht_gatter = NichtGatter()

    def pruefe_zustand(self):
        self.und_gatter.setze_eingangA(self.eingangA)
        self.und_gatter.setze_eingangB(self.eingangB)
        self.und_gatter.pruefe_zustand()
        ergebnis_und = self.und_gatter.ausgang
        self.nicht_gatter.setze_eingangA(ergebnis_und)
        self.nicht_gatter.pruefe_zustand()
        self.ausgang = self.nicht_gatter.ausgang

print("Teste alle möglichen Eingänge für das Nicht-Und Gatter...")
nichtundgatter = NichtUndGatter()
gatterAusgeben(nichtundgatter)

class NichtOderGatter(Logikgatter):
    def __init__(self):
        self.oder_gatter = ORGatter()
        self.nicht_gatter = NichtGatter()

    def pruefe_zustand(self):
        self.oder_gatter.setze_eingangA(self.eingangA)
        self.oder_gatter.setze_eingangB(self.eingangB)
        self.oder_gatter.pruefe_zustand()
        ergebnis_oder = self.oder_gatter.ausgang
        self.nicht_gatter.setze_eingangA(ergebnis_oder)
        self.nicht_gatter.pruefe_zustand()
        self.ausgang = self.nicht_gatter.ausgang

print("Teste alle möglichen Eingänge für das Nicht-Oder Gatter...")
nichtodergatter = NichtOderGatter()
gatterAusgeben(nichtodergatter)


