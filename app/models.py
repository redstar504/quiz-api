from django.db import models


# Create your models here.
class Topic(models.Model):
    title = models.CharField(max_length=30)
    icon = models.CharField(max_length=30)
    color = models.CharField(max_length=30)
    statkey = models.CharField(max_length=60, blank=True, null=True)


class Question(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    question = models.CharField(max_length=255)


class QuestionOption(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    is_correct = models.BooleanField(default=False)
    option = models.CharField(max_length=255)
