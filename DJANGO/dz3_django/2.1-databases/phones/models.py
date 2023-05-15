from django.db import models
from django.template.defaultfilters import slugify


class Phone(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    image = models.CharField(max_length=250)
    release_date = models.CharField(max_length=10)
    lte_exists = models.BooleanField()
    slug = models.SlugField(null=False, unique=True)

    def save(self, *args, **kwargs):  # new
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)
