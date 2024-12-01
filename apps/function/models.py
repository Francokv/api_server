from django.db import models


class ServerlessFunction(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    code = models.TextField()
    runtime = models.CharField(max_length=255)
    memory_size = models.IntegerField()
    timeout = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    project = models.ForeignKey('project.Project', on_delete=models.CASCADE)

    def __str__(self):
        return self.name