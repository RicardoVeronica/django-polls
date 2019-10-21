from django.db import models


class Question(models.Model):
    """
    Database question and published data
    """
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('Fecha de publicación')


class Choise(models.Model):
    """
    Database choise text and votes count
    """
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choise_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
