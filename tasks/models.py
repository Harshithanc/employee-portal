from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(
        max_length=20,
        choices=[
            ('Pending', 'Pending'),
            ('Completed', 'Completed')
        ],
        default='Pending'
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
