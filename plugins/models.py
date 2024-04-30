from django.db import models
from cms.models import CMSPlugin
# Create your models here.
class Properties(CMSPlugin):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)

    @property
    def get_full_url(self):
        try:
            return self.placeholder.page.get_absolute_url()
        except AttributeError:
            return ""