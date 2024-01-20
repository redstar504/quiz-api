from django.db import models


# Create your models here.
class Topic(models.Model):
    title = models.CharField(max_length=30)
    icon = models.CharField(max_length=30)
    color = models.CharField(max_length=30)


class Question(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    question = models.CharField(max_length=60)


class QuestionOption(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    option = models.CharField(max_length=60)
