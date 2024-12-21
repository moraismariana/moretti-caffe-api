from rest_framework import serializers
from moretti.models import Categoria, Prato, EstatisticasGerais, Acesso, InicioTexto, InicioBg, SobreTexto, SobreBg, SobreImg, CardapioTexto, CardapioBg

# Cardápio

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'

class PratoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prato
        fields = "__all__"


# Estatísticas de visitantes

class AcessoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Acesso
        fields = "__all__"

class EstatisticasGeraisSerializer(serializers.ModelSerializer):
    class Meta:
        model = EstatisticasGerais
        fields = "__all__"


# Edição de conteúdo CMS

class InicioTextoSerializer(serializers.ModelSerializer):
    class Meta:
        model = InicioTexto
        fields = "__all__"

class InicioBgSerializer(serializers.ModelSerializer):
    class Meta:
        model = InicioBg
        fields = "__all__"

class SobreTextoSerializer(serializers.ModelSerializer):
    class Meta:
        model = SobreTexto
        fields = "__all__"

class SobreBgSerializer(serializers.ModelSerializer):
    class Meta:
        model = SobreBg
        fields = "__all__"

class SobreImgSerializer(serializers.ModelSerializer):
    class Meta:
        model = SobreImg
        fields = "__all__"

class CardapioTextoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CardapioTexto
        fields = "__all__"

class CardapioBgSerializer(serializers.ModelSerializer):
    class Meta:
        model = CardapioBg
        fields = "__all__"