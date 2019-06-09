from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class TodoNote(models.Model):
    
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    is_done = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{}".format(self.title)

    class Meta:
        ordering = ["-created_at"]

class TodoList(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    task = models.CharField(max_length=255)
    PRIORITY_TASK = [
    ('LO', 'LOW'),
    ('ME', 'MEDIUM'),
    ('HI', 'HIGH'),
    ]
    priority = models.CharField(
        max_length=2,choices=PRIORITY_TASK,
        default='ME',
    )
    is_done = models.BooleanField(default=False)
    due_by = models.DateTimeField(
        blank=True,
        null=True,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return "{}".format(self.task)

    class Meta:
        ordering = ["-created_at"]
