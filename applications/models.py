from django.db import models
from django.conf import settings
from jobs.models import Job

class Application(models.Model):
    PENDING = 'P'
    REVIEWED = 'R'
    REJECTED = 'X'
    STATUS_CHOICES = [
        (PENDING, 'Pending'),
        (REVIEWED, 'Reviewed'),
        (REJECTED, 'Rejected'),
    ]

    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='applications')
    applicant = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='applications')
    cover_letter = models.TextField(blank=True)
    resume_url = models.URLField(blank=True, null=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default=PENDING)
    applied_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.job.title} - {self.applicant.username}"
