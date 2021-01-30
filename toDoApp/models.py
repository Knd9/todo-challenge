from django.db import models


class ToDo(models.Model):
    """
    Define ToDo object model that contains:
    a content of ToDo (title, description),
    the cration date with time (creationDate)
    and done status (completed)
    """

    creationDate = models.DateTimeField(auto_now_add=True, editable=False)
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    completed = models.BooleanField(null=False, default=False)

    def __str__(self):
        return self.title
