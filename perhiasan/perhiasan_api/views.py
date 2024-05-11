from rest_framework import viewsets
from .models import Kategori, Produk, Pembelian
from .serializers import KategoriSerializer, ProdukSerializer, PembelianSerializer

class KategoriViewSet(viewsets.ModelViewSet):
    queryset = Kategori.objects.all()
    serializer_class = KategoriSerializer

class ProdukViewSet(viewsets.ModelViewSet):
    queryset = Produk.objects.all()
    serializer_class = ProdukSerializer

class PembelianViewSet(viewsets.ModelViewSet):
    queryset = Pembelian.objects.all()
    serializer_class = PembelianSerializer
