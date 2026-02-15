# from django.db import models

# Create your models here.

# superuser - username - Saumya
# pass - Somu@2001 email- saumyakantbaral2001@gmail.com

from django.db import models

class Skill(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    technologies = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class Experience(models.Model):
    company = models.CharField(max_length=200)
    role = models.CharField(max_length=200)
    duration = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.company
