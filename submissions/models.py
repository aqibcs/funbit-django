from django.db import models
from django.contrib.auth.models import User
from challenges.models import Challenge
from django.utils import timezone

class Submission(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    challenge = models.ForeignKey(Challenge, on_delete=models.CASCADE)
    text_response = models.TextField(blank=True, null=True)
    image_response = models.ImageField(upload_to='submissions/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user.username}'s submission for {self.challenge.title}"
    
    class Meta:
        unique_together = ('user', 'challenge', 'created_at')
        
    def likes_count(self):
        return self.like_set.count()

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    submission = models.ForeignKey(Submission, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ('user', 'submission')
