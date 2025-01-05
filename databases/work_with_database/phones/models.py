from xmlrpc.client import Boolean

from django.db.models import Model, IntegerField, CharField, DateField, BooleanField, URLField, SlugField


class Phone(Model):
    id = IntegerField(primary_key=True)
    name = CharField(max_length=200)
    price = IntegerField(null=True, blank=True)
    image = URLField(null=True, blank=True)
    release_date = DateField(null=True, blank=True)
    lte_exists = BooleanField(null=True, blank=True)
    slug = SlugField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name


