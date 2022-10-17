from django.db import models


class Phone(models.Model):
    # TODO: Добавьте требуемые поля

    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=32)
    price = models.IntegerField(u'Цена')
    image = models.TextField(u'Изображение')
    release_date = models.DateField()
    lte_exists = models.BooleanField()
    slug = models.SlugField(u'URL', unique=True, blank=True)