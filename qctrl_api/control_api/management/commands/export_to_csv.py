from control_api.models import Control
from django.core.management.base import BaseCommand


class Command(BaseCommand):

    def handle(self, *args, **options):
       Control.objects.to_csv('../assets/export.csv')