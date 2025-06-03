from django.contrib.sessions.models import Session
from django.core.management.base import BaseCommand

def clear_sessions():
    Session.objects.all().delete()
    print("Все сессии очищены.")

# Для автоматического вызова при старте сервера
class Command(BaseCommand):
    def handle(self, *args, **options):
        clear_sessions()