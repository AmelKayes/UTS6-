from django.urls import path, include
from rest_framework.routers import DefaultRouter
from perhiasan_api.views import KategoriViewSet, ProdukViewSet, PembelianViewSet

router = DefaultRouter()
router.register(r'kategori', KategoriViewSet)
router.register(r'produk', ProdukViewSet)
router.register(r'pembelian', PembelianViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
