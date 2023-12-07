from django.contrib.auth.models import User
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "A brief description of your custom command"

    def handle(self, *args, **options):
        names = [
            "Alice",
            "Bob",
            "Charlie",
            "David",
            "Eva",
            "Frank",
            "Grace",
            "Hank",
            "Ivy",
            "Jack",
        ]
        for name in names:
            print(name)
            username = name.lower()
            password = "password123"
            User.objects.create_user(username=username, password=password)

        print("users created")
