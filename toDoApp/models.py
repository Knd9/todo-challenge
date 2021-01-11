from django.db import models

# Create your models here.
class ToDo(models.Model):
    creationDate = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    completed = models.BooleanField(null=False, default=False)

    def __str__(self):
        return str(self.id)
    