from rest_framework import serializers
from django.contrib.auth.models import User
from .models import (
    EmployerProfile, CandidateProfile, 
    JobListing, Resume, JobApplication
)

class UserRegistrationSerializer(serializers.ModelSerializer):
    """Handles user registration"""
    password = serializers.CharField(write_only=True, min_length=8)
    password2 = serializers.CharField(write_only=True, min_length=8)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2', 'first_name', 'last_name']

    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError("Passwords don't match!")
        return data

    def create(self, validated_data):
        validated_data.pop('password2')
        user = User.objects.create_user(**validated_data)
        return user

class EmployerProfileSerializer(serializers.ModelSerializer):
    user_email = serializers.EmailField(source='user.email', read_only=True)
    user_full_name = serializers.SerializerMethodField()

    class Meta:
        model = EmployerProfile
        fields = '__all__'
        read_only_fields = ['user', 'created_at']

    def get_user_full_name(self, obj):
        return obj.user.get_full_name()

class CandidateProfileSerializer(serializers.ModelSerializer):
    user_email = serializers.EmailField(source='user.email', read_only=True)
    user_full_name = serializers.SerializerMethodField()

    class Meta:
        model = CandidateProfile
        fields = '__all__'
        read_only_fields = ['user', 'created_at']

    def get_user_full_name(self, obj):
        return obj.user.get_full_name()

class JobListingSerializer(serializers.ModelSerializer):
    employer_name = serializers.CharField(source='employer.company_name', read_only=True)
    application_count = serializers.SerializerMethodField()

    class Meta:
        model = JobListing
        fields = '__all__'
        read_only_fields = ['employer', 'created_at', 'updated_at']

    def get_application_count(self, obj):
        return obj.applications.count()

class ResumeSerializer(serializers.ModelSerializer):
    candidate_name = serializers.CharField(source='candidate.user.username', read_only=True)

    class Meta:
        model = Resume
        fields = '__all__'
        read_only_fields = ['candidate', 'uploaded_at']

class JobApplicationSerializer(serializers.ModelSerializer):
    candidate_name = serializers.CharField(source='candidate.user.get_full_name', read_only=True)
    job_title = serializers.CharField(source='job.title', read_only=True)
    company_name = serializers.CharField(source='job.employer.company_name', read_only=True)

    class Meta:
        model = JobApplication
        fields = '__all__'
        read_only_fields = ['candidate', 'applied_at', 'updated_at']

class JobApplicationStatusUpdateSerializer(serializers.ModelSerializer):
    """Special serializer just for updating application status"""
    class Meta:
        model = JobApplication
        fields = ['status', 'employer_notes']