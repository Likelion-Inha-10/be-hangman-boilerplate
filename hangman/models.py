from django.db import models

# Create your models here.
class Hangman_Game(models.Model):
    word=models.CharField(max_length=50,null=True)
    max_try=models.IntegerField(null=True)
    try_count=models.IntegerField(null=True)
    hidden_chars=models.CharField(max_length=50,null=True)
    try_chars=models.CharField(max_length=50,null=True)
    answer=models.CharField(max_length=50,null=True)
    
