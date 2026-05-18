from rest_framework import viewsets, permissions, status, filters
from rest_framework.decorators import action, api_view, permission_classes
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from .models import (
    EmployerProfile, CandidateProfile, 
    JobListing, Resume, JobApplication
)
from .serializers import (
    UserRegistrationSerializer, EmployerProfileSerializer,
    CandidateProfileSerializer, JobListingSerializer,
    ResumeSerializer, JobApplicationSerializer,
    JobApplicationStatusUpdateSerializer
)

@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def register_user(request):
    """Register a new user (either employer or candidate)"""
    serializer = UserRegistrationSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        
        # Create the appropriate profile based on user type
        user_type = request.data.get('user_type', '').lower()
        if user_type == 'employer':
            EmployerProfile.objects.create(
                user=user,
                company_name=request.data.get('company_name', ''),
                company_description=request.data.get('company_description', '')
            )
        elif user_type == 'candidate':
            CandidateProfile.objects.create(user=user)
        
        return Response({
            'message': 'User registered successfully!',
            'user_id': user.id,
            'username': user.username
        }, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EmployerProfileViewSet(viewsets.ModelViewSet):
    """ViewSet for employer profiles"""
    queryset = EmployerProfile.objects.all()  # MAKE SURE THIS EXISTS
    serializer_class = EmployerProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        # Automatically assign the current user as the employer
        serializer.save(user=self.request.user)

    @action(detail=False, methods=['get'])
    def my_profile(self, request):
        """Get the current user's employer profile"""
        profile = get_object_or_404(EmployerProfile, user=request.user)
        serializer = self.get_serializer(profile)
        return Response(serializer.data)

class CandidateProfileViewSet(viewsets.ModelViewSet):
    """ViewSet for candidate profiles"""
    queryset = CandidateProfile.objects.all()  # MAKE SURE THIS EXISTS
    serializer_class = CandidateProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @action(detail=False, methods=['get'])
    def my_profile(self, request):
        """Get the current user's candidate profile"""
        profile = get_object_or_404(CandidateProfile, user=request.user)
        serializer = self.get_serializer(profile)
        return Response(serializer.data)

class JobListingViewSet(viewsets.ModelViewSet):
    """ViewSet for job listings"""
    queryset = JobListing.objects.filter(is_active=True)  # THIS EXISTS BUT LET'S VERIFY
    serializer_class = JobListingSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'description', 'requirements', 'location']
    ordering_fields = ['created_at', 'title', 'salary_range']
    ordering = ['-created_at']  # Default ordering: newest first

    def get_permissions(self):
        """Custom permissions based on action"""
        if self.action in ['create', 'update', 'partial_update', 'destroy', 'my_listings']:
            return [permissions.IsAuthenticated()]
        return [permissions.AllowAny()]

    def perform_create(self, serializer):
        """Automatically assign employer when creating a job"""
        employer_profile = get_object_or_404(EmployerProfile, user=self.request.user)
        serializer.save(employer=employer_profile)

    @action(detail=False, methods=['get'])
    def my_listings(self, request):
        """Get all jobs posted by the current employer"""
        employer_profile = get_object_or_404(EmployerProfile, user=request.user)
        jobs = JobListing.objects.filter(employer=employer_profile)
        serializer = self.get_serializer(jobs, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def search(self, request):
        """Search jobs with filters"""
        queryset = self.filter_queryset(self.get_queryset())
        
        # Apply additional filters
        job_type = request.query_params.get('job_type')
        location = request.query_params.get('location')
        
        if job_type:
            queryset = queryset.filter(job_type=job_type)
        if location:
            queryset = queryset.filter(location__icontains=location)
        
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

class ResumeViewSet(viewsets.ModelViewSet):
    """ViewSet for resumes"""
    queryset = Resume.objects.all()  # THIS IS THE FIX - ADD DEFAULT QUERYSET
    serializer_class = ResumeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        """Override to filter based on user"""
        if hasattr(self.request.user, 'candidateprofile'):
            return Resume.objects.filter(candidate__user=self.request.user)
        return Resume.objects.none()

    def perform_create(self, serializer):
        """Automatically assign candidate when uploading resume"""
        candidate_profile = get_object_or_404(CandidateProfile, user=self.request.user)
        serializer.save(candidate=candidate_profile)

class JobApplicationViewSet(viewsets.ModelViewSet):
    """ViewSet for job applications"""
    queryset = JobApplication.objects.all()  # ADD DEFAULT QUERYSET HERE TOO
    serializer_class = JobApplicationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        """Show different applications based on user type"""
        user = self.request.user
        
        # If the user is an employer, show applications for their jobs
        if hasattr(user, 'employerprofile'):
            return JobApplication.objects.filter(
                job__employer__user=user
            ).order_by('-applied_at')
        
        # If the user is a candidate, show their applications
        elif hasattr(user, 'candidateprofile'):
            return JobApplication.objects.filter(
                candidate__user=user
            ).order_by('-applied_at')
        
        return JobApplication.objects.none()

    def perform_create(self, serializer):
        """Automatically assign candidate when applying"""
        candidate_profile = get_object_or_404(CandidateProfile, user=self.request.user)
        serializer.save(candidate=candidate_profile)

    @action(detail=True, methods=['patch'])
    def update_status(self, request, pk=None):
        """Allow employers to update application status"""
        application = self.get_object()
        
        # Check if the user is the employer who posted this job
        if not hasattr(request.user, 'employerprofile') or \
           application.job.employer.user != request.user:
            return Response(
                {"error": "Only the job poster can update application status"},
                status=status.HTTP_403_FORBIDDEN
            )
        
        serializer = JobApplicationStatusUpdateSerializer(
            application, data=request.data, partial=True
        )
        
        if serializer.is_valid():
            serializer.save()
            return Response({
                'message': 'Application status updated successfully',
                'application': JobApplicationSerializer(application).data
            })
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['get'])
    def my_applications(self, request):
        """Get all applications for the current user"""
        if hasattr(request.user, 'candidateprofile'):
            applications = JobApplication.objects.filter(
                candidate__user=request.user
            ).order_by('-applied_at')
            serializer = self.get_serializer(applications, many=True)
            return Response(serializer.data)
        return Response(
            {"error": "Only candidates can view their applications"},
            status=status.HTTP_400_BAD_REQUEST
        )