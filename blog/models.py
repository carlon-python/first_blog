from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='images/',null=True, blank=True)
    description = models.CharField(max_length=150)
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
