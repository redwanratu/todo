from django.db import models

# Create your models here.

class Task(models.Model):
    title=models.CharField(max_length=100)
    done=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title


