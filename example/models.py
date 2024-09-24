from django.db import models


class Volunteer(models.Model):
    TGID = models.CharField(max_length=100, unique=True)
    username = models.CharField(max_length=150)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    address = models.TextField()
    highest_education = models.CharField(max_length=100)
    is_employed = models.BooleanField()
    needs = models.TextField()
    bio = models.TextField(blank=True, null=True)
    profile_pic = models.URLField(blank=True, null=True)
    is_joined_group = models.BooleanField(default=False)
    joined_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username
