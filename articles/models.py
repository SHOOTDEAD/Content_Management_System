from django.db import models

# Model to store articles
class Article(models.Model):
    title = models.CharField(max_length=100,null=False)
    files = models.FileField(blank=True,upload_to='static/article/files/')
    content = models.TextField(null=False)
    date = models.DateField(null=False)
    author = models.TextField(null=False)
    tags = models.TextField(null=False)


   