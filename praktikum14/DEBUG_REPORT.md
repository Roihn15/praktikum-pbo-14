# DEBUG REPORT

## Bug PPN 10%

Bug: Harga akhir menjadi lebih besar/kecil dari seharusnya.

### Langkah Debugging
1. Aktifkan pdb.set_trace()
2. Jalankan program
3. Periksa variabel:
   - p harga_awal
   - p jumlah_diskon
   - p harga_akhir

### Temuan
PPN 10% dihitung dua kali sehingga harga akhir tidak sesuai.

### Solusi
Hilangkan perhitungan PPN tambahan.
