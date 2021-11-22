import unittest
from ostoskori import Ostoskori
from tuote import Tuote


class TestOstoskori(unittest.TestCase):
    def setUp(self):
        self.kori = Ostoskori()

    def test_ostoskorin_hinta_ja_tavaroiden_maara_alussa(self):
        self.assertEqual(self.kori.hinta(), 0)
        self.assertEqual(self.kori.tavaroita_korissa(), 0)

    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_tavara(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)

        self.assertEqual(self.kori.tavaroita_korissa(), 1)

    def test_yhden_lisaamisen_jalkeen_korin_hinta_tuotteen_hinta(self):
        maito = Tuote('Maito', 3)
        self.kori.lisaa_tuote(maito)

        self.assertEqual(self.kori.hinta(), 3)

    def test_kaksi_eri_tuotetta_palauttaa_ostoskorin_koon_oikein(self):
        maito = Tuote('Maito', 3)
        leipa = Tuote('Leipa', 6)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(leipa)

        self.assertEqual(self.kori.tavaroita_korissa(), 2)

    def test_kaksi_eri_tuotetta_palauttaa_ostoskorin_hinnan_oikein(self):
        maito = Tuote('Maito', 3)
        leipa = Tuote('Leipa', 6)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(leipa)

        self.assertEqual(self.kori.hinta(), 9)

    def test_kaksi_samaa_tuotetta_palauttaa_ostoskorin_koon_oikein(self):
        maito = Tuote('Maito', 3)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(maito)

        self.assertEqual(self.kori.tavaroita_korissa(), 2)

    def test_kaksi_samaa_tuotetta_palauttaa_ostoskorin_koon_oikein(self):
        maito = Tuote('Maito', 3)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(maito)

        self.assertEqual(self.kori.hinta(), 6)
