from django.db import models



class Sign(models.Model):
    user_id = models.CharField(max_length=10)
    user_pw = models.CharField(max_length=10)
    def __str__(self):
        return self.user_id