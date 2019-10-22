import datetime

from django.db import models
from django.utils import timezone


class Question(models.Model):
    """
    Database question and published data
    """
    question_text = models.CharField('Pregunta', max_length=200)
    pub_date = models.DateTimeField('Fecha de publicación')

    class Meta:
        verbose_name = "Pregunta"
        verbose_name_plural = "Preguntas"

    def was_published_recently(self):
        """
        Return a date with timezone
        """
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    was_published_recently.admin_order_filed = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = '¿Publicado hoy?'

    def __str__(self):
        """
        Return question_text as representation of an object
        """
        return self.question_text


class Choice(models.Model):
    """
    Database choice text and votes count
    """
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField('Elección', max_length=200)
    votes = models.IntegerField('Votos', default=0)

    def __str__(self):
        """
        Return choice_text like representation of an object
        """
        return self.choice_text
