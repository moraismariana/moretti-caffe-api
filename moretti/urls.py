from django.urls import path, include

from moretti.views import CategoriaViewSet, PratoViewSet, EstatisticasGeraisViewSet, AcessoViewSet, AcessoResumoView, InicioTextoViewSet, InicioBgViewSet, SobreTextoViewSet, SobreBgViewSet, SobreImgViewSet, CardapioTextoViewSet, CardapioBgViewSet
from rest_framework import routers

router_moretti = routers.DefaultRouter()
router_moretti.register('categorias', CategoriaViewSet, basename='categorias')
router_moretti.register('pratos', PratoViewSet, basename='pratos')
router_moretti.register('estatisticas-gerais', EstatisticasGeraisViewSet, basename='estatisticas-gerais')
router_moretti.register('acessos', AcessoViewSet, basename='acessos')
router_moretti.register('iniciotexto', InicioTextoViewSet, basename='iniciotexto')
router_moretti.register('iniciobg', InicioBgViewSet, basename='iniciobg')
router_moretti.register('sobretexto', SobreTextoViewSet, basename='sobretexto')
router_moretti.register('sobrebg', SobreBgViewSet, basename='sobrebg')
router_moretti.register('sobreimg', SobreImgViewSet, basename='sobreimg')
router_moretti.register('cardapiotexto', CardapioTextoViewSet, basename='cardapiotexto')
router_moretti.register('cardapiobg', CardapioBgViewSet, basename='cardapiobg')

urlpatterns = [
    path('', include(router_moretti.urls)),
    path('acessos/resumo/30/', AcessoResumoView.as_view(), {'dias': 30}, name='acessos-resumo-30'),
    path('acessos/resumo/15/', AcessoResumoView.as_view(), {'dias': 15}, name='acessos-resumo-15'),
    path('acessos/resumo/7/', AcessoResumoView.as_view(), {'dias': 7}, name='acessos-resumo-7'),
    path('acessos/resumo/1/', AcessoResumoView.as_view(), {'dias': 0}, name='acessos-resumo-1'),
]