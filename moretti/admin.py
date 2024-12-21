from django.contrib import admin
from moretti.models import Categoria, Prato, EstatisticasGerais, Acesso, InicioTexto, InicioBg, SobreTexto, SobreBg, SobreImg, CardapioTexto, CardapioBg

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    list_display_links = ('nome',)

class PratoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome',)
    list_display_links = ('id', 'nome',)
    list_filter = ('categoria',)

class EstatisticasGeraisAdmin(admin.ModelAdmin):
    list_display = ('id',)
    list_display_links = ('id',)

class AcessoAdmin(admin.ModelAdmin):
    list_display = ('id',)
    list_display_links = ('id',)

class InicioTextoAdmin(admin.ModelAdmin):
    list_display = ('id',)
    list_display_links = ('id',)

class InicioBgAdmin(admin.ModelAdmin):
    list_display = ('id',)
    list_display_links = ('id',)

class SobreTextoAdmin(admin.ModelAdmin):
    list_display = ('id',)
    list_display_links = ('id',)

class SobreBgAdmin(admin.ModelAdmin):
    list_display = ('id',)
    list_display_links = ('id',)

class SobreImgAdmin(admin.ModelAdmin):
    list_display = ('id',)
    list_display_links = ('id',)

class CardapioTextoAdmin(admin.ModelAdmin):
    list_display = ('id',)
    list_display_links = ('id',)

class CardapioBgAdmin(admin.ModelAdmin):
    list_display = ('id',)
    list_display_links = ('id',)


admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Prato, PratoAdmin)
admin.site.register(EstatisticasGerais, EstatisticasGeraisAdmin)
admin.site.register(InicioTexto, InicioTextoAdmin)
admin.site.register(Acesso, AcessoAdmin) 
admin.site.register(InicioBg, InicioBgAdmin)
admin.site.register(SobreTexto, SobreTextoAdmin)
admin.site.register(SobreBg, SobreBgAdmin)
admin.site.register(SobreImg, SobreImgAdmin)
admin.site.register(CardapioTexto, CardapioTextoAdmin)
admin.site.register(CardapioBg, CardapioBgAdmin)