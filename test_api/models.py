from django.db import models


# Create your models here.

class Answer(models.Model):
    text = models.CharField(max_length=256)

    def __str__(self):
        return self.text


class Polls(models.Model):
    name = models.CharField(max_length=64)
    start_date = models.DateField(auto_now=True, editable=False)
    finish_date = models.DateField()
    definition = models.CharField(max_length=256)
    answer_text = models.ForeignKey(Answer, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class UserAnswer(models.Model):
    user_id = models.CharField(max_length=64)
    answered_text = models.CharField(max_length=256)
    answered_poll = models.ForeignKey(Polls, on_delete=models.CASCADE)
