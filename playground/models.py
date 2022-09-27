from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)


class Person(models.Model):
    name = models.CharField(max_length=100, verbose_name="full name")


class Offer(models.Model):
    RefNo = models.CharField(max_length=200)
    City = models.CharField(max_length=200)
    Deadline = models.CharField(max_length=200)

    def __str__(self):
        return self.RefNo
