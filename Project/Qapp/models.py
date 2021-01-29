from django.db import models

########Answer용 모델을 만든다???????  담아라 숫자로
class Answer(models.Model):
    ans=models.CharField(default="", max_length=10, null=True, blank=True)

class Question(models.Model):
    question = models.CharField(max_length=100)

    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    
    img = models.ImageField(max_length=100, null=True, blank=True)

    answer = models.CharField(max_length=100)   #admin answer에 1234로 번호로 바꿔야함???
    
    def __str__(self):
        # return self.question
        return str(self.id)+"번 문제"


class User(models.Model):
    name = models.CharField(max_length=30)
    # quiz_url = models.URLField(max_length=200, null=True, blank=True, unique=True)
    answer = models.CharField(default="", max_length=10, null=True, blank=True)
#answer:숫자로 1234중 선택한거
    result = models.IntegerField(default=0, null=True, blank=True)
#result: 맞은 개수

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['result', 'name']