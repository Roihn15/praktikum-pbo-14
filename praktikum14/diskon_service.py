class DiskonCalculator:
    def hitung_diskon(self, harga_awal, persen_diskon):
        if harga_awal <= 0:
            return 0
        jumlah_diskon = harga_awal * (persen_diskon / 100)
        harga_akhir = harga_awal - jumlah_diskon
        return harga_akhir

if __name__ == "__main__":
    calc = DiskonCalculator()
    print(calc.hitung_diskon(10000, 10))
