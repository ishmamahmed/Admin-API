from django.db import models

# This is my Admin model
class SysAdmin(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    description = models.TextField()

    def __str__(self):
        return self.name


