KAPASITEETTI = 5
OLETUSKASVATUS = 5


class IntJoukko:
    def __init__(self, kapasiteetti=KAPASITEETTI, kasvatuskoko=OLETUSKASVATUS):
        self.kapasiteetti = kapasiteetti
        self.kasvatuskoko = kasvatuskoko
        self.ljono = [None] * self.kapasiteetti
        self.alkioiden_lkm = 0

    def kuuluu(self, n):
        return n in self.ljono

    def lisaa(self, n):
        if n in self.ljono:
            return False

        if self.alkioiden_lkm == self.kapasiteetti:
            self.kapasiteetti += self.kasvatuskoko
            self.ljono = self.ljono + ([0] * self.kasvatuskoko)

        self.ljono[self.alkioiden_lkm] = n
        self.alkioiden_lkm += 1
        return True

    def poista(self, n):
        if not self.kuuluu(n):
            return False

        kohta = self.ljono.index(n)
        print(self.ljono)
        for i in range(kohta, self.alkioiden_lkm-1):
            print(self.ljono[i], self.ljono[i+1])
            self.ljono[i] = self.ljono[i+1]
        else:
            self.ljono[self.alkioiden_lkm-1] = None
        self.alkioiden_lkm -= 1
        print(self.ljono)
        return True

    def kopioi_taulukko(self, a, b):
        b = a[:]

    def mahtavuus(self):
        return self.alkioiden_lkm

    def to_int_list(self):
        taulu = [0] * self.alkioiden_lkm

        for i in range(0, len(taulu)):
            taulu[i] = self.ljono[i]

        print(taulu)
        print(list(filter(lambda x: x != None, self.ljono)))

        return taulu  # list(filter(lambda x: x != None, self.ljono))

    @staticmethod
    def yhdiste(a, b):
        x = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            x.lisaa(a_taulu[i])

        for i in range(0, len(b_taulu)):
            x.lisaa(b_taulu[i])

        return x

    @staticmethod
    def leikkaus(a, b):
        y = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            for j in range(0, len(b_taulu)):
                if a_taulu[i] == b_taulu[j]:
                    y.lisaa(b_taulu[j])

        return y

    @staticmethod
    def erotus(a, b):
        z = IntJoukko()
        a_taulu = a.to_int_list()
        # print(a_taulu)
        b_taulu = b.to_int_list()
        # print(b_taulu)

        for i in range(0, len(a_taulu)):
            z.lisaa(a_taulu[i])
            print(z.ljono, '+', a_taulu[i])

        for i in range(0, len(b_taulu)):
            z.poista(b_taulu[i])
            print(z.ljono, '-', b_taulu[i])

        return z

    def __str__(self):
        if self.alkioiden_lkm == 0:
            return "{}"
        elif self.alkioiden_lkm == 1:
            return "{" + str(self.ljono[0]) + "}"
        else:
            tuotos = "{"
            for i in range(0, self.alkioiden_lkm - 1):
                tuotos = tuotos + str(self.ljono[i])
                tuotos = tuotos + ", "
            tuotos = tuotos + str(self.ljono[self.alkioiden_lkm - 1])
            tuotos = tuotos + "}"
            return tuotos
