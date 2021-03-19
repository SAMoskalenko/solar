from django.db import models


class Sites(models.Model):
    name = models.CharField(max_length=50)
    url = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)
    last_check = models.DateTimeField()

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = 'site'
        verbose_name_plural = "sites"
