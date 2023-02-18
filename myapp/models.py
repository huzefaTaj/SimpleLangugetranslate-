from django.db import models

class Article(models.Model):
    title = models. JSONField('Article title', default=dict)
    content = models.TextField(null=True)

