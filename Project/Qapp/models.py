from django.db import models

class Question(models.Model):
    question = models.CharField(max_length=100)

    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    
    img = models.ImageField(max_length=100, null=True, blank=True)

    answer = models.CharField(max_length=100)
    
    def __str__(self):
        return self.question