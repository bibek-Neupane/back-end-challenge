from csv import DictReader
from django.core.management import BaseCommand
from control_api.models import Control

class Command(BaseCommand):
    def handle(self, *args, **options):
        if Control.objects.exists():
            print('control data already loaded')
            return
        print("Uploading Control Data...")
        for row in DictReader(open('../assets/controls.csv')):
            control = Control()
            control.name = row['name']
            control.type = row['type']
            control.maximum_rabi_rate = row['maximum_rabi_rate']
            control.polar_angle = row['polar_angle']
            control.save()