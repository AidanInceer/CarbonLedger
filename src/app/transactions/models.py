from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class UserProfile(models.Model):
    """Extended user profile with preferences."""
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    theme = models.CharField(max_length=10, choices=[('light', 'Light'), ('dark', 'Dark')], default='light')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username}'s profile"


class Project(models.Model):
    """A project/workspace for organizing transactions."""
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='projects')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        unique_together = ['owner', 'name']

    def __str__(self):
        return f"{self.name} ({self.owner.username})"


class Transaction(models.Model):
    """Model representing a coffee shop transaction."""
    
    CATEGORY_CHOICES = [
        ('beverage', 'Beverage'),
        ('food', 'Food'),
        ('merchandise', 'Merchandise'),
        ('other', 'Other'),
    ]
    
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='transactions')
    date = models.DateTimeField(default=timezone.now)
    item_name = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    customer_name = models.CharField(max_length=100, blank=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='beverage')

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return f"{self.item_name} - ${self.amount} ({self.date.strftime('%Y-%m-%d %H:%M')})"


class ProjectMember(models.Model):
    """Model representing a member of a project."""
    
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('member', 'Member'),
        ('viewer', 'Viewer'),
    ]
    
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='members')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='project_memberships')
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='member')
    joined_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['project', 'user']

    def __str__(self):
        return f"{self.user.username} - {self.project.name} ({self.role})"
