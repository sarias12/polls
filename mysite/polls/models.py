    """Models Module
    """
from django.db import models


class Question(models.Model):
    """
    Model for a question and a publicacion date
    """
    question_text = models.CharField(max_length=200)
    pub_date = models.DataTimeField('date published')

class Choice(models.Model):
    """
    Model for fields (choice's test and  vote tall)
    """
    question_text = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
