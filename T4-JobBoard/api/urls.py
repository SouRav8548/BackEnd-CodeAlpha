from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# Create a router for ViewSets
router = DefaultRouter()
router.register(r'employers', views.EmployerProfileViewSet)
router.register(r'candidates', views.CandidateProfileViewSet)
router.register(r'jobs', views.JobListingViewSet)
router.register(r'resumes', views.ResumeViewSet, basename='resume')  # ADD basename HERE
router.register(r'applications', views.JobApplicationViewSet)


urlpatterns = [
    # Include all router URLs
    path('', include(router.urls)),
    
    # Custom endpoint for user registration
    path('register/', views.register_user, name='register'),
    
    # Authentication endpoints (login/logout)
    path('auth/', include('rest_framework.urls')),
]