from django.conf import settings
from django.core.management.base import BaseCommand
from utils.tasks import testing

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        testing.delay()
