from django.db import models

class Sign(models.Model):
    iid = models.CharField(max_length=10)
    ppw = models.IntegerField(default=0)
    def __str__(self):
        return self.iid
