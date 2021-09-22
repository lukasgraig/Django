from django.db import models

# Create your models here.

URGENCY = (
    (0, "Low"),
    (1, "Medium"),
    (2, "High"),
)

class CheckList(models.Model):
    title = models.CharField(max_length=100, blank=True)
    description = models.TextField(max_length=150, blank=False)
    status = models.IntegerField(choices=URGENCY, default=0)
    completed = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title