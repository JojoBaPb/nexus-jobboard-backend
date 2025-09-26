from rest_framework import serializers
from .models import Job, Category, Company


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug']


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['id', 'name', 'website']


class JobSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    company = CompanySerializer(read_only=True)

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

    posted_by = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Job
        fields = [
            'id', 'title', 'description',
            'company', 'company_id',
            'category', 'category_id',
            'location', 'job_type',
            'is_active', 'posted_by',
            'posted_at', 'slug'
        ]
