import csv

from django.core.management.base import BaseCommand
from phones.models import Phone
from django.template.defaultfilters import slugify

class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as csvfile:

            phone_reader = list(csv.DictReader(csvfile, delimiter=';'))
            # пропускаем заголовок
            # next(phone_reader)

            for phone in phone_reader:
                # TODO: Добавьте сохранение модели
                new_item = Phone.objects.create(
                    id=phone['id'],
                    name=phone['name'],
                    image=phone['image'],
                    price=phone['price'],
                    release_date=phone['release_date'],
                    lte_exists=phone['lte_exists'],
                    slug=slugify(phone['name']),
                )



