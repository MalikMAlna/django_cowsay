from django.db import models


class Text(models.Model):
    text = models.CharField(max_length=5000)

    def __str__(self):
        return self.text
