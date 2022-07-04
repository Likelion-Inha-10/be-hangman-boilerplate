from django.db import models

class Hangman(models.Model):
    try_count = models.IntegerField(null=True)
    max_try = models.IntegerField(null=True)
    tried_chars = models.CharField(max_length=50, null=True)
    word = models.CharField(max_length=50, null=True)
    hidden = models.CharField(max_length=50, null=True)
    ans = models.CharField(max_length=50, null=True)