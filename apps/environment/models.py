from django.db import models




class Environment(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    project = models.ForeignKey('project.Project', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class EnvironmentVariable(models.Model):
    name = models.CharField(max_length=100)
    value = models.TextField()
    environment = models.ForeignKey(Environment, on_delete=models.CASCADE)

    def __str__(self):
        return self.name