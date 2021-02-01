
from django.db import models


class ToDo(models.Model):
    title = models.CharField(max_length=240, help_text='What needs to be done?')
    is_completed = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'ToDo'
        verbose_name_plural = 'ToDos'

    def __str__(self):
        return self.title
