from rest_framework import serializers
from .models import Application

class ApplicationSerializer(serializers.ModelSerializer):
    applicant = serializers.StringRelatedField(read_only=True)
    job_title = serializers.CharField(source='job.title', read_only=True)

    class Meta:
        model = Application
        fields = ['id', 'applicant', 'job', 'job_title', 'resume', 'cover_letter', 'status', 'applied_at']
        read_only_fields = ['applicant', 'status', 'applied_at']
