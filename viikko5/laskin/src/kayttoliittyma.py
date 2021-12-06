from enum import Enum
from tkinter import ttk, constants, StringVar
from komentotehdas import Komentotehdas, Komento


class Kayttoliittyma:
    def __init__(self, sovellus, root):
        self._sovellus = sovellus
        self._root = root
        self._komentotehdas = Komentotehdas(
            self._sovellus, {"hae_arvo": self._hae_arvo, "aseta_arvo": self._aseta_arvo, "aseta_kumoaminen": self._aseta_kumoaminen})
        self._kumottavaa = False

    def kaynnista(self):
        self._tulos_var = StringVar()
        self._tulos_var.set(self._sovellus.tulos)
        self._syote_kentta = ttk.Entry(master=self._root)

        self.tulos_teksti = ttk.Label(textvariable=self._tulos_var)

        self.summa_painike = ttk.Button(
            master=self._root,
            text="Summa",
            command=lambda: self._suorita_komento(Komento.SUMMA)
        )

        self.erotus_painike = ttk.Button(
            master=self._root,
            text="Erotus",
            command=lambda: self._suorita_komento(Komento.EROTUS)
        )

        self._nollaus_painike = ttk.Button(
            master=self._root,
            text="Nollaus",
            state=constants.DISABLED,
            command=lambda: self._suorita_komento(Komento.NOLLAUS)
        )

        self._kumoa_painike = ttk.Button(
            master=self._root,
            text="Kumoa",
            state=constants.DISABLED,
            command=lambda: self._suorita_komento(Komento.KUMOA)
        )

        self.tulos_teksti.grid(columnspan=4)
        self._syote_kentta.grid(
            columnspan=4, sticky=(constants.E, constants.W))
        self.summa_painike.grid(row=2, column=0)
        self.erotus_painike.grid(row=2, column=1)
        self._nollaus_painike.grid(row=2, column=2)
        self._kumoa_painike.grid(row=2, column=3)

    def _hae_arvo(self):
        arvo = 0

        try:
            arvo = int(self._syote_kentta.get())
        except Exception:
            pass

        return arvo

    def _aseta_arvo(self, arvo):
        self._nollaus_painike["state"] = constants.DISABLED if arvo == 0 else constants.NORMAL
        self._syote_kentta.delete(0, constants.END)
        self._tulos_var.set(arvo)

    def _aseta_kumoaminen(self, voiko):
        self._kumottavaa = voiko

    def _suorita_komento(self, komento):
        self._komentotehdas.hae(komento).suorita()
        self._kumoa_painike["state"] = constants.NORMAL if self._kumottavaa else constants.DISABLED
