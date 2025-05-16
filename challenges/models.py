from django.db import models
import random


class Challenge(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    points = models.IntegerField(default=10)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    requires_image = models.BooleanField(default=False)
    requires_text = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    @classmethod
    def get_random_challenge(cls):
        active_challenges = cls.objects.filter(is_active=True)
        if active_challenges.exists():
            return random.choice(active_challenges)
        return None
