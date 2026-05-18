from django.contrib import admin
from .models import (
    EmployerProfile, CandidateProfile, 
    JobListing, Resume, JobApplication
)

@admin.register(EmployerProfile)
class EmployerProfileAdmin(admin.ModelAdmin):
    list_display = ['company_name', 'user', 'created_at']
    search_fields = ['company_name', 'user__username']

@admin.register(CandidateProfile)
class CandidateProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'location', 'created_at']
    search_fields = ['user__username', 'user__email']

@admin.register(JobListing)
class JobListingAdmin(admin.ModelAdmin):
    list_display = ['title', 'employer', 'job_type', 'location', 'is_active', 'created_at']
    list_filter = ['job_type', 'is_active', 'created_at']
    search_fields = ['title', 'description', 'employer__company_name']
    list_editable = ['is_active']  # Can toggle active status directly

@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display = ['candidate', 'experience_years', 'uploaded_at']
    search_fields = ['candidate__user__username', 'skills']

@admin.register(JobApplication)
class JobApplicationAdmin(admin.ModelAdmin):
    list_display = ['job', 'candidate', 'status', 'applied_at']
    list_filter = ['status', 'applied_at']
    search_fields = ['job__title', 'candidate__user__username']
    list_editable = ['status']