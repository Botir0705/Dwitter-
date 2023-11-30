from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


class Profile(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE)
    follows = models.ManyToManyField(
        'self', 
        related_name='followed_by',
        blank=True,
        symmetrical=False
        )


    def __str__(self):
        return f'{str(self.username)}'
    
# class DweetManager(models.Manager):
#     def create_dweet(self, author, body):
#         dweet = self.create(author=request.user)
class Dweet(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField(default='')
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.body[:20]}... by {self.author}'
    

def create_profile(sender, instance, created, **kwargs):
    if created:
        user_profile = Profile(username=instance)
        user_profile.save()
        user_profile.follows.set([instance.profile.id])
        user_profile.save()

# Create a Profile for each new user.
post_save.connect(create_profile, sender=User)
