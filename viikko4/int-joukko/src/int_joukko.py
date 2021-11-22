KAPASITEETTI = 5
OLETUSKASVATUS = 5


class IntJoukko:
    def __init__(self, kapasiteetti=KAPASITEETTI, kasvatuskoko=OLETUSKASVATUS):
        self.kapasiteetti = kapasiteetti
        self.kasvatuskoko = kasvatuskoko
        self.ljono = [0] * self.kapasiteetti
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
        # kohta = -1
        # apu = 0

        # for i in range(0, self.alkioiden_lkm):
        #     if n == self.ljono[i]:
        #         kohta = i  # siis luku löytyy tuosta kohdasta :D
        #         self.ljono[kohta] = 0
        #         break

        # if kohta != -1:
        #     for j in range(kohta, self.alkioiden_lkm - 1):
        #         apu = self.ljono[j]
        #         self.ljono[j] = self.ljono[j + 1]
        #         self.ljono[j + 1] = apu

        #     self.alkioiden_lkm = self.alkioiden_lkm - 1
        #     return True

        # return False
        if not self.kuuluu(n):
            return False

        kohta = self.ljono.index(n)
        self.ljono[kohta] = 0

        for i in range(kohta, self.alkioiden_lkm-1):
            self.ljono[i] = self.ljono[i+1]
        self.alkioiden_lkm -= 1

        return True

    def kopioi_taulukko(self, a, b):
        for i in range(0, len(a)):
            b[i] = a[i]

    def mahtavuus(self):
        return self.alkioiden_lkm

    def to_int_list(self):
        taulu = [0] * self.alkioiden_lkm

        for i in range(0, len(taulu)):
            taulu[i] = self.ljono[i]

        return taulu

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
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            z.lisaa(a_taulu[i])

        for i in range(0, len(b_taulu)):
            z.poista(b_taulu[i])

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
