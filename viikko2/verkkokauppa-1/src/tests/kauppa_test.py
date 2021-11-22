import unittest
from unittest.mock import Mock, ANY
from kauppa import Kauppa
from viitegeneraattori import Viitegeneraattori
from varasto import Varasto
from tuote import Tuote


class TestKauppa(unittest.TestCase):
    def setUp(self):
        self.pankki_mock = Mock()
        self.viitegeneraattori_mock = Mock()
        self.viitegeneraattori_mock.uusi.return_value = 42
        self.varasto_mock = Mock()

        def varasto_saldo(tid):
            if tid == 1:
                return 999
            if tid == 2:
                return 123
            if tid == 3:
                return 0

        def varasto_hae_tuote(tid):
            if tid == 1:
                return Tuote(1, "HKBLÅ", 10)
            if tid == 2:
                return Tuote(2, "HK not so BLÅ", 5)
            if tid == 3:
                return Tuote(3, "HK bättre BLÅ", 15)

        self.varasto_mock.saldo.side_effect = varasto_saldo
        self.varasto_mock.hae_tuote.side_effect = varasto_hae_tuote
        self.kauppa = Kauppa(
            self.varasto_mock, self.pankki_mock, self.viitegeneraattori_mock)

    def test_ostoksen_paaytyttya_pankin_metodia_tilisiirto_kutsutaan(self):

        # tehdään ostokset
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")

        # varmistetaan, että metodia tilisiirto on kutsuttu
        self.pankki_mock.tilisiirto.assert_called()
        # toistaiseksi ei välitetä kutsuun liittyvistä argumenteista

    def test_ostoksen_paatyttya_pankin_metodia_tilisiirto_kutsutaan_oikeilla_argumenteilla(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")

        self.pankki_mock.tilisiirto.assert_called_with(
            'pekka', 42, '12345', '33333-44455', 10)

    def test_kahden_eri_tuotteen_jalkeen_pankin_metodia_tilisiirto_kutsutaan_oikeilla_argumenteilla(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(2)
        self.kauppa.tilimaksu('pekka', '12345')

        self.pankki_mock.tilisiirto.assert_called_with(
            'pekka', 42, '12345', '33333-44455', 15)

    def test_kahden_saman_tuotteen_jalkeen_pankin_metodia_tilisiirto_kutsutaan_oikeilla_argumenteilla(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu('pekka', '12345')

        self.pankki_mock.tilisiirto.assert_called_with(
            'pekka', 42, '12345', '33333-44455', 20)

    def test_varastossa_olevan_ja_loppuolevan_tuotteen_jalkeen_pankin_metodia_tilisiirto_kutsutaan_oikeilla_argumenteilla(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(3)
        self.kauppa.tilimaksu('pekka', '12345')

        self.pankki_mock.tilisiirto.assert_called_with(
            'pekka', 42, '12345', '33333-44455', 10)

    def test_uusi_asiakas_nollaa_edellisen(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(2)
        self.kauppa.tilimaksu('seppo', '54321')

        self.pankki_mock.tilisiirto.assert_called_with(
            'seppo', 42, '54321', '33333-44455', 5)

    def test_aina_uusi_viitenumero(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu('pekka', 42)

        self.viitegeneraattori_mock.uusi.assert_called()

        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(2)
        self.kauppa.tilimaksu('seppo', '54321')

        self.viitegeneraattori_mock.uusi.assert_called()

    def test_poista_korista_poistaa_sinne_lisätyn(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(2)
        self.kauppa.poista_korista(2)

        self.varasto_mock.hae_tuote.assert_called()

        self.kauppa.tilimaksu('pekka', '12345')

        self.pankki_mock.tilisiirto.assert_called_with(
            'pekka', 42, '12345', '33333-44455', 10)
