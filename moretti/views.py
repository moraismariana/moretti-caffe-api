from rest_framework import viewsets, permissions
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny
from rest_framework.response import Response
import json

from datetime import timedelta
from django.utils import timezone
from rest_framework.views import APIView

from moretti.models import Categoria, Prato, EstatisticasGerais, Acesso, InicioTexto, InicioBg, SobreTexto, SobreBg, SobreImg, CardapioTexto, CardapioBg

from moretti.serializers import CategoriaSerializer, PratoSerializer, EstatisticasGeraisSerializer, AcessoSerializer, InicioTextoSerializer, InicioBgSerializer, SobreTextoSerializer, SobreBgSerializer, SobreImgSerializer, CardapioTextoSerializer, CardapioBgSerializer

class PermissaoMoretti(permissions.BasePermission):
    """
    Permissão personalizada para verificar se o usuário faz parte do grupo de editores.
    """
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        # Verifica se o usuário está no grupo 'Editores Moretti'
        return request.user.groups.filter(name='Editores Moretti').exists()

# Cardápio

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, PermissaoMoretti]

class PratoViewSet(viewsets.ModelViewSet):
    queryset = Prato.objects.all()
    serializer_class = PratoSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, PermissaoMoretti]


# Estatísticas de visitantes

class AcessoViewSet(viewsets.ModelViewSet):
    queryset = Acesso.objects.all()
    serializer_class = AcessoSerializer
    permission_classes = [AllowAny]
    
    # Função para interpretar corretamente dados que forem enviados através do sendBeacon() no javaScript
    def create(self, request, *args, **kwargs):
        if request.content_type.startswith('text/plain'):
            data = json.loads(request.body.decode('utf-8'))
            serializer = self.get_serializer(data=data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            return Response(serializer.data, status=201)
        
        return super().create(request, *args, **kwargs)

class AcessoResumoView(APIView):
    """
    View que retorna um resumo de contagens de objetos filtrados por período.
    """
    def get_queryset(self, dias):
        """
        Filtra os objetos Acesso de acordo com o número de dias.
        """
        data_inicio = timezone.now().date() - timedelta(days=dias)
        return Acesso.objects.filter(data__gte=data_inicio)

    def get(self, request, dias):
        """
        Calcula as contagens e retorna o resumo em formato JSON.
        """
        queryset = self.get_queryset(dias)

        # Contagem total de acessos
        total_acessos = queryset.count()

        # Contagens específicas baseadas nos campos booleanos
        revisitas = queryset.filter(revisita=True).count()
        acessos_cardapio = queryset.filter(acesso_cardapio=True).count()
        acessos_pagina_inicial = queryset.filter(acesso_pagina_inicial=True).count()
        acessos_sobre = queryset.filter(acesso_sobre=True).count()
        toques_link_contato = queryset.filter(toque_contato=True).count()

        # Monta o resumo
        resumo = {
            "acessos": total_acessos,
            "revisitas": revisitas,
            "acessos_cardapio": acessos_cardapio,
            "acessos_pagina_inicial": acessos_pagina_inicial,
            "acessos_sobre": acessos_sobre,
            "toques_link_contato": toques_link_contato,
        }

        return Response(resumo)

class EstatisticasGeraisViewSet(viewsets.ModelViewSet):
    queryset = EstatisticasGerais.objects.all()
    serializer_class = EstatisticasGeraisSerializer


# Edição de conteúdo CMS

class InicioTextoViewSet(viewsets.ModelViewSet):
    queryset = InicioTexto.objects.all()
    serializer_class = InicioTextoSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, PermissaoMoretti]

class InicioBgViewSet(viewsets.ModelViewSet):
    queryset = InicioBg.objects.all()
    serializer_class = InicioBgSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, PermissaoMoretti]

class SobreTextoViewSet(viewsets.ModelViewSet):
    queryset = SobreTexto.objects.all()
    serializer_class = SobreTextoSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, PermissaoMoretti]

class SobreBgViewSet(viewsets.ModelViewSet):
    queryset = SobreBg.objects.all()
    serializer_class = SobreBgSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, PermissaoMoretti]

class SobreImgViewSet(viewsets.ModelViewSet):
    queryset = SobreImg.objects.all()
    serializer_class = SobreImgSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, PermissaoMoretti]

class CardapioTextoViewSet(viewsets.ModelViewSet):
    queryset = CardapioTexto.objects.all()
    serializer_class = CardapioTextoSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, PermissaoMoretti]

class CardapioBgViewSet(viewsets.ModelViewSet):
    queryset = CardapioBg.objects.all()
    serializer_class = CardapioBgSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, PermissaoMoretti]