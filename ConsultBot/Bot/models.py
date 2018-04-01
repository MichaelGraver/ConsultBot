from django.db import models

# Create your models here.
class Statements(models.Model):
    readonly_fields=('id',)
    statement = models.TextField()
    topic = models.CharField(max_length=40)
    sentiment = models.CharField(max_length=40)
    counters = models.CharField(max_length=200)
    response = models.TextField(default="")
    def __str__(self):
        return (str(self.id) + " " + self.statement)
    class Meta:
        verbose_name_plural = "Statements"

class Sessions(models.Model):
    SessionKey = models.CharField(max_length=40)
    StatementPath = models.TextField()
    TemplatesUsed = models.BooleanField(default=False)
    ReasonGiven = models.BooleanField(default=False)
    TopicComplete = models.BooleanField(default=False)
    CurrentStatement = models.CharField(max_length=100, default="")
    CurrentTopic = models.CharField(max_length=100, default="")
    Topics = models.CharField(max_length=200)
    def __str__(self):
        return self.SessionKey
    class Meta:
        verbose_name_plural = "Sessions"       

class Questionnaire(models.Model):
    SessionKey = models.CharField(max_length=40)
    Question1 = models.CharField(max_length=40)
    Question2 = models.CharField(max_length=40)
    Question3 = models.CharField(max_length=40)
    Question4 = models.CharField(max_length=40)
    Question5 = models.CharField(max_length=40)
    Question6 = models.CharField(max_length=40)
    Question7 = models.TextField(max_length=40)
    Question8 = models.TextField(max_length=40)
    def __str__(self):
        return self.SessionKey
    class Meta:
        verbose_name_plural = "Questionnaire Results"  
