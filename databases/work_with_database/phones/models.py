from xmlrpc.client import Boolean

from django.db.models import Model, IntegerField, CharField, DateField, BooleanField, URLField, SlugField


class Phone(Model):
    id = IntegerField(primary_key=True)
    name = CharField(max_length=200)
    price = IntegerField()
    image = URLField()
    release_date = DateField()
    lte_exists = BooleanField()
    slug = SlugField(max_length=200)

    def __str__(self):
        return self.name


