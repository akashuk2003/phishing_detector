from django.db import models

class SearchHistory(models.Model):
    url = models.URLField(max_length=500)
    result = models.CharField(max_length=50)
    confidence_score = models.FloatField()
    search_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.url} - {self.result}"