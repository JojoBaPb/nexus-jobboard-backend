from rest_framework import serializers
from .models import Application
from jobs.serializers import JobSerializer
from django.contrib.auth import get_user_model

User = get_user_model()


# -------------------------------
# Applicant Serializer
# -------------------------------
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']  #More can be added if needed


# -------------------------------
# Application Serializer
# -------------------------------
class ApplicationSerializer(serializers.ModelSerializer):
    job = JobSerializer(read_only=True)       # Show full job details
    job_id = serializers.PrimaryKeyRelatedField(
        queryset=Application._meta.get_field('job').related_model.objects.all(),
        write_only=True,
        source='job'
    )
    applicant = UserSerializer(read_only=True)  # Show user info instead of raw ID

    class Meta:
        model = Application
        fields = [
            'id',
            'job', 'job_id',
            'applicant',
            'cover_letter',
            'created_at',
            'status'
        ]
        read_only_fields = ['id', 'created_at', 'status']

