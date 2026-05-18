from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class EmployerProfile(models.Model):
    """Stores information about employers/companies"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=200)
    company_description = models.TextField(help_text="Describe your company")
    company_website = models.URLField(blank=True, null=True)
    company_logo = models.ImageField(upload_to='company_logos/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.company_name

    class Meta:
        verbose_name = "Employer Profile"
        verbose_name_plural = "Employer Profiles"

class CandidateProfile(models.Model):
    """Stores information about job seekers"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20, blank=True)
    location = models.CharField(max_length=200, blank=True)
    professional_summary = models.TextField(blank=True, help_text="Brief summary of your experience")
    linkedin_url = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.get_full_name() or self.user.username

    class Meta:
        verbose_name = "Candidate Profile"
        verbose_name_plural = "Candidate Profiles"

class JobListing(models.Model):
    """Stores job postings created by employers"""
    JOB_TYPES = [
        ('FT', 'Full Time'),
        ('PT', 'Part Time'),
        ('CT', 'Contract'),
        ('FR', 'Freelance'),
        ('IN', 'Internship'),
    ]

    employer = models.ForeignKey(
        EmployerProfile, 
        on_delete=models.CASCADE, 
        related_name='job_listings'
    )
    title = models.CharField(max_length=200)
    description = models.TextField()
    requirements = models.TextField(help_text="List the required skills and qualifications")
    location = models.CharField(max_length=200)
    salary_range = models.CharField(max_length=100, blank=True, help_text="e.g., $50,000 - $70,000")
    job_type = models.CharField(max_length=2, choices=JOB_TYPES, default='FT')
    is_active = models.BooleanField(default=True, help_text="Uncheck to hide this listing")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} at {self.employer.company_name}"

    class Meta:
        ordering = ['-created_at']  # Newest jobs first
        verbose_name = "Job Listing"
        verbose_name_plural = "Job Listings"

class Resume(models.Model):
    """Stores candidate resumes"""
    candidate = models.OneToOneField(
        CandidateProfile, 
        on_delete=models.CASCADE, 
        related_name='resume'
    )
    file = models.FileField(upload_to='resumes/', help_text="Upload your resume (PDF or Word)")
    skills = models.TextField(help_text="Comma-separated list of skills (e.g., Python, Django, React)")
    experience_years = models.IntegerField(default=0)
    education = models.TextField(blank=True, help_text="Your educational background")
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Resume of {self.candidate.user.username}"

    class Meta:
        verbose_name = "Resume"
        verbose_name_plural = "Resumes"

class JobApplication(models.Model):
    """Stores job applications from candidates"""
    STATUS_CHOICES = [
        ('PENDING', 'Pending Review'),
        ('REVIEWING', 'Under Review'),
        ('SHORTLISTED', 'Shortlisted'),
        ('REJECTED', 'Rejected'),
        ('ACCEPTED', 'Accepted'),
    ]

    job = models.ForeignKey(
        JobListing, 
        on_delete=models.CASCADE, 
        related_name='applications'
    )
    candidate = models.ForeignKey(
        CandidateProfile, 
        on_delete=models.CASCADE, 
        related_name='applications'
    )
    resume = models.ForeignKey(Resume, on_delete=models.SET_NULL, null=True)
    cover_letter = models.TextField(blank=True, help_text="Why are you a good fit for this role?")
    status = models.CharField(
        max_length=20, 
        choices=STATUS_CHOICES, 
        default='PENDING'
    )
    employer_notes = models.TextField(blank=True, help_text="Internal notes about the candidate")
    applied_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.candidate.user.username} applied for {self.job.title}"

    class Meta:
        unique_together = ['job', 'candidate']  # Prevents duplicate applications
        ordering = ['-applied_at']
        verbose_name = "Job Application"
        verbose_name_plural = "Job Applications"