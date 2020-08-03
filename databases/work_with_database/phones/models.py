from django.db import models


class Phone(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, default=None, unique=True)
    price = models.IntegerField()
    image = models.URLField()
    release_date = models.DateField()
    lte_exists = models.BooleanField()

    class Meta:
        db_table = 'phones'
