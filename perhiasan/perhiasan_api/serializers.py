from rest_framework import serializers
from .models import Kategori, Produk, Pembelian

class KategoriSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kategori
        fields = '__all__'

class ProdukSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produk
        fields = '__all__'

class PembelianSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pembelian
        fields = '__all__'
