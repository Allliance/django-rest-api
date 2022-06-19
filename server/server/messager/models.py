from django.db import models
from django.utils import timezone
from . import constants


class Client(models.Model):
    username = models.TextField(max_length=40, unique=True)
    port = models.IntegerField(unique=True)
    date_modified = models.DateTimeField(auto_now=True)

    @property
    def is_present(self):
        return self.date_modified + constants.AWAKE_INTERVAL >= timezone.now()
