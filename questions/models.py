from django.contrib.auth.models import AbstractUser
from django.db import models

class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True


class User(AbstractUser):
    phone = models.CharField(max_length=13)
    email = models.EmailField(blank=True,null=True)

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self):
        return self.username



class Question(models.Model):
    text = models.TextField()

    class Meta:
        verbose_name = "question"
        verbose_name_plural = "questions"

    def __str__(self):
        return self.text

class Option(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE,related_name="options")
    is_correct = models.BooleanField(default=False)
    text = models.CharField(max_length=255)

    class Meta:
        verbose_name = "option"
        verbose_name_plural = "options"

    def __str__(self):
        return f"{self.text}({'Correct' if self.is_correct else 'Incorrect'})"


class Result(models.Model):
    user = models.ForeignKey(User,null=True,blank=True, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    selected_option = models.ForeignKey(Option, on_delete=models.CASCADE)
    is_correct = models.BooleanField(default=False)
    score = models.BooleanField(default=False)

    class Meta:
        verbose_name = "result"
        verbose_name_plural = "results"
        unique_together = ("user", "question")

    def __str__(self):
        return f"{self.user.username} - {self.question.text} ({self.score})"

    def save(self , *args,**kwargs):
        self.is_correct = self.selected_option.is_correct
        super().save(*args, **kwargs)
