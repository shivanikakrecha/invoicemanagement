from django.db import models
from accounts import choices
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User

# Create your models here.


class TimeStamps(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class UserProfile(TimeStamps, models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    display_name = models.CharField(max_length=250, blank=True, null=True)
    user_type = models.CharField(
        choices=choices.USER_TYPE_CHOICES, default=None, max_length=15, blank=True, null=True)
    profile_description = models.TextField(
        max_length=999, blank=True, null=True)
    phone_number = models.CharField(max_length=255, blank=True, null=True)
    mobile_number = models.CharField(max_length=255, blank=True, null=True)
    email_notification = models.BooleanField(default=True)
    agents = models.ManyToManyField("self", blank=True, null=True)
    reporting_to = models.ForeignKey(
        "self", on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.user.username

    def get_full_name(self):
        """
        Returns the first_name plus the last_name, with a space in between.
        """
        full_name = '{} {}'.format(self.user.first_name, self.user.last_name)
        return full_name.strip()

    def is_manager(self):
        if self.user_type == "manager":
            return True
        return False
