from enum import Enum


class Komento(Enum):
    SUMMA = 1
    EROTUS = 2
    NOLLAUS = 3
    KUMOA = 4


class Komentotehdas:
    def __init__(self, sovellus, io):

        self.sovellus = sovellus
        self.io = io

        self._komennot = {
            Komento.SUMMA: Summa(self.sovellus, self.io),
            Komento.EROTUS: Erotus(self.sovellus, self.io),
            Komento.NOLLAUS: Nollaus(self.sovellus, self.io),
            Komento.KUMOA: Tuntematon()
        }

    def hae(self, komento):
        return self._komennot[komento] if komento in self._komennot else Tuntematon()


class Summa:
    def __init__(self, sovellus, io):
        self.sovellus = sovellus
        self.io = io

    def suorita(self):
        arvo = self.io["hae_arvo"]()
        self.sovellus.plus(arvo)
        self.io["aseta_arvo"](self.sovellus.tulos)


class Erotus:
    def __init__(self, sovellus, io):
        self.sovellus = sovellus
        self.io = io

    def suorita(self):
        arvo = self.io["hae_arvo"]()
        self.sovellus.miinus(arvo)
        self.io["aseta_arvo"](self.sovellus.tulos)


class Nollaus:
    def __init__(self, sovellus, io):
        self.sovellus = sovellus
        self.io = io

    def suorita(self):
        self.sovellus.nollaa()
        self.io["aseta_arvo"](self.sovellus.tulos)


class Tuntematon:
    def __init__(self):
        pass

    def suorita(self):
        pass
