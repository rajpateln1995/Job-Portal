from django.db import models
from django.urls import reverse
from django.utils import timezone

from accounts.models import User

JOB_TYPE = (
    ('1', "Plumbing"),
    ('2', "Carpentry"),
    ('3', "Masonary"),
    ('4',"Electrical Repair"),
)


class Job(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=300)
    description = models.TextField()
    location = models.CharField(max_length=150)
    category = models.CharField(choices=JOB_TYPE, max_length=20)
    last_date = models.DateTimeField()
    company_name = models.CharField(max_length=100)
    website = models.CharField(max_length=100, default="")
    created_at = models.DateTimeField(default=timezone.now)
    filled = models.BooleanField(default=False)
    living_space = models.BooleanField(default=False)
    electricity = models.BooleanField(default=False)
    wage = models.IntegerField(default=0, blank=True)

    def get_absolute_url(self):
        return reverse('jobs:jobs-detail', args=[self.id])

    def __str__(self):
        return self.title


class Applicant(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='applicants')
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        unique_together = ['user', 'job']

    def __str__(self):
        return self.user.get_full_name()
