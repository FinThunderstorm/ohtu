from tuote import Tuote
from ostos import Ostos


class Ostoskori:
    def __init__(self):
        self.__ostokset = {}
        # ostoskori tallettaa Ostos-oliota, yhden per korissa oleva Tuote

    def tavaroita_korissa(self):
        maara = 0
        for ostos in self.__ostokset.values():
            maara += ostos.lukumaara()

        return maara
        # kertoo korissa olevien tavaroiden lukumäärän
        # eli jos koriin lisätty 2 kpl tuotetta "maito", tulee metodin palauttaa 2
        # samoin jos korissa on 1 kpl tuotetta "maito" ja 1 kpl tuotetta "juusto", tulee metodin palauttaa 2

    def hinta(self):
        hinta = 0
        for ostos in self.__ostokset.values():
            hinta += ostos.hinta()

        return hinta
        # kertoo korissa olevien ostosten yhteenlasketun hinnan

    def lisaa_tuote(self, lisattava: Tuote):
        # lisää tuotteen
        if lisattava.nimi() not in self.__ostokset.keys():
            self.__ostokset[lisattava.nimi()] = Ostos(lisattava)
            return

        self.__ostokset[lisattava.nimi()].muuta_lukumaaraa(1)

    def poista_tuote(self, poistettava: Tuote):
        # poistaa tuotteen
        if poistettava.nimi() in self.__ostokset.keys():
            self.__ostokset[poistettava.nimi()].muuta_lukumaaraa(-1)
        if self.__ostokset[poistettava.nimi()].lukumaara() == 0:
            del self.__ostokset[poistettava.nimi()]

    def tyhjenna(self):
        for ostos in list(self.__ostokset.keys()):
            del self.__ostokset[ostos]
        # tyhjentää ostoskorin

    def ostokset(self):
        return list(self.__ostokset.values())
        # palauttaa listan jossa on korissa olevat ostos-oliot
        # kukin ostos-olio siis kertoo mistä tuotteesta on kyse JA kuinka monta kappaletta kyseistä tuotetta korissa on
