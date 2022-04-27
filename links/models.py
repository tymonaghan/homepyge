from django.db import models

# Create your models here.
class Link(models.Model):
    link_title = models.CharField("Title", max_length=40)
    link_descrip = models.CharField("Link Description",max_length=200)
    link_url = models.URLField("Link URL")