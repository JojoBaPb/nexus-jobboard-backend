from rest_framework import serializers
from .models import Job, Category, Company
from django.contrib.auth import get_user_model

User = get_user_model()


# -------------------------------
# Category Serializer
# -------------------------------
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug']


# -------------------------------
# Company Serializer
# -------------------------------
class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['id', 'name', 'website']


# -------------------------------
# User (Posted By) Serializer
# -------------------------------
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']
        ref_name = "JobsUser"   #unique schema name for this serializer


# -------------------------------
# Job Serializer
# -------------------------------
class JobSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    company = CompanySerializer(read_only=True)
    posted_by = UserSerializer(read_only=True)  # ✅ Show user info
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(),
        write_only=True,
        source='category'
    )
    company_id = serializers.PrimaryKeyRelatedField(
        queryset=Company.objects.all(),
        write_only=True,
        source='company'
    )

    class Meta:
        model = Job
        fields = [
            'id', 'title', 'description',
            'company', 'company_id',
            'category', 'category_id',
            'location', 'job_type',
            'is_active', 'posted_by', 'posted_at', 'slug'
        ]
