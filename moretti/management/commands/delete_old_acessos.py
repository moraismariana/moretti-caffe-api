from django.core.management.base import BaseCommand
from moretti.models import Acesso
from datetime import timedelta
from django.utils import timezone

class Command(BaseCommand):
    help = 'Deleta registros do modelo Acesso com mais de 30 dias'

    def handle(self, *args, **kwargs):
        threshold_date = timezone.now().date() - timedelta(days=30)
        deleted_count, _ = Acesso.objects.filter(data__lt=threshold_date).delete()
        self.stdout.write(self.style.SUCCESS(f'{deleted_count} registros deletados com sucesso.'))
