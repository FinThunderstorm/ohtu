from enum import Enum


class Komento(Enum):
    TUNTEMATON = 0
    SUMMA = 1
    EROTUS = 2
    NOLLAUS = 3
    KUMOA = 4


class Komentotehdas:
    def __init__(self, sovellus, io):

        self.sovellus = sovellus
        self.io = io
        self.edellinen = []

        self._komennot = {
            Komento.SUMMA: Summa(self.sovellus, self.io),
            Komento.EROTUS: Erotus(self.sovellus, self.io),
            Komento.NOLLAUS: Nollaus(self.sovellus, self.io),
            Komento.KUMOA: Kumoa(self.sovellus, self.io, self.edellinen)
        }

    def hae(self, komento):
        if komento in self._komennot:
            if komento != Komento.KUMOA:
                self.edellinen.append(komento)
            return self._komennot[komento]
        return Tuntematon()


class Summa:
    edellinen = None

    def __init__(self, sovellus, io):
        self._sovellus = sovellus
        self._io = io

    def suorita(self):
        arvo = self._io["hae_arvo"]()
        Summa.edellinen = self._sovellus.tulos
        self._sovellus.plus(arvo)
        self._io["aseta_arvo"](self._sovellus.tulos)
        self._io["aseta_kumoaminen"](True)

    def kumoa(self):
        self._sovellus.aseta_arvo(Summa.edellinen)
        self._io["aseta_arvo"](Summa.edellinen)


class Erotus:
    edellinen = None

    def __init__(self, sovellus, io):
        self._sovellus = sovellus
        self._io = io

    def suorita(self):
        arvo = self._io["hae_arvo"]()
        Erotus.edellinen = self._sovellus.tulos
        self._sovellus.miinus(arvo)
        self._io["aseta_arvo"](self._sovellus.tulos)
        self._io["aseta_kumoaminen"](True)

    def kumoa(self):
        self._sovellus.aseta_arvo(Erotus.edellinen)
        self._io["aseta_arvo"](Erotus.edellinen)


class Nollaus:
    edellinen = None

    def __init__(self, sovellus, io):
        self._sovellus = sovellus
        self._io = io

    def suorita(self):
        Nollaus.edellinen = self._sovellus.tulos
        self._sovellus.nollaa()
        self._io["aseta_arvo"](self._sovellus.tulos)
        self._io["aseta_kumoaminen"](True)

    def kumoa(self):
        self._sovellus.aseta_arvo(Nollaus.edellinen)
        self._io["aseta_arvo"](Nollaus.edellinen)


class Kumoa:
    def __init__(self, sovellus, io, edellinen):
        self._sovellus = sovellus
        self._io = io
        self._edellinen = edellinen
        self._kumottavat = {
            Komento.SUMMA: Summa(self._sovellus, self._io),
            Komento.EROTUS: Erotus(self._sovellus, self._io),
            Komento.NOLLAUS: Nollaus(self._sovellus, self._io)
        }

    def suorita(self):
        kumottava = self._edellinen.pop()
        print('kumotaan', kumottava)
        self._kumottavat[kumottava].kumoa()
        if len(self._edellinen) == 0:
            self._io["aseta_kumoaminen"](False)


class Tuntematon:
    def __init__(self):
        pass

    def suorita(self):
        pass

    def kumoa(self):
        pass
