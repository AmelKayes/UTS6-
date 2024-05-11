from django.db import models

class Kategori(models.Model):
    nama = models.CharField(max_length=100)

    def __str__(self):
        return self.nama

class Produk(models.Model):
    nama = models.CharField(max_length=100)
    harga = models.DecimalField(max_digits=10, decimal_places=2)
    kategori = models.ForeignKey(Kategori, related_name='produk', on_delete=models.CASCADE)

    def __str__(self):
        return self.nama

class Pembelian(models.Model):
    produk = models.ForeignKey(Produk, related_name='pembelian', on_delete=models.CASCADE)
    jumlah = models.IntegerField()
    tanggal = models.DateField()

    def __str__(self):
        return f"{self.produk} - {self.tanggal}"
