from django.db import models
from django.urls import reverse
from django.utils import timezone

# Create your models here.

class Announcement(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.CharField(max_length=100, default="Anonymous")
    date_created = models.DateTimeField(default=timezone.now)
    is_published = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['-date_created']
        
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('announcement_detail', kwargs={'pk': self.pk})
    
    def get_preview(self):
        """Return first 150 characters for preview"""
        if len(self.content) > 150:
            return self.content[:150] + "..."
        return self.content
