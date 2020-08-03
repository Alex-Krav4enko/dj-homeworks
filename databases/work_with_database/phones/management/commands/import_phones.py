import csv
from django.core.management.base import BaseCommand
from django.template.defaultfilters import slugify
from phones.models import Phone


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as csvfile:
            phone_reader = csv.DictReader(csvfile, delimiter=';')

            for line in phone_reader:
                phone = Phone(
                    id=int(line['id']),
                    name=line['name'],
                    slug=slugify(line['name']),
                    price=int(line['price']),
                    image=line['image'],
                    release_date=line['release_date'],
                    lte_exists=bool(line['lte_exists']),
                )
                phone.save()
