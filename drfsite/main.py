import os

import django
import random

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'drfsite.settings')
django.setup()

from todoapp.models import *
from faker import Faker

fake = Faker('ru-RU')

# Добавление Списков
for _ in range(5):
    List.objects.create(name=fake.sentence(nb_words=1),
                        color=fake.color())

# Добавление Задач
for _ in range(20):
    Task.objects.create(list=List.objects.get(pk=random.choice(List.objects.all().values_list('id', flat=True))),
                        importance=Importance.objects.get(pk=random.choice(Importance.objects.all().values_list('id', flat=True))),
                        title=fake.sentence(nb_words=2),
                        description=fake.sentence(nb_words=5),
                        date='2023-04-12 03:00:00.000000+0300',
                        status=False)
