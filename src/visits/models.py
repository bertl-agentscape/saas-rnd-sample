from django.db import models


class PageVisit(models.Model):
    page = models.CharField(max_length=120)
    count = models.IntegerField(default=0)
    path = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.page} - {self.count}"
