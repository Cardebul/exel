from django.db import models

# Create your models here.


class XLModel(models.Model):
    name = models.CharField(max_length=30)
    data = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    

