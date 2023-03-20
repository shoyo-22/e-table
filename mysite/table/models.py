from django.db import models


class WeekDay(models.Model):
    day_of_week = models.CharField(max_length=200)

    def __str__(self):
        return self.day_of_week


class Subjects(models.Model):
    day = models.ForeignKey(WeekDay, on_delete=models.CASCADE)
    subject = models.CharField(max_length=200)

    def __str__(self):
        return self.subject
