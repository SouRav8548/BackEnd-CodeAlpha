# 🎯 Job Board Platform - Backend API

A full-featured Job Board Platform backend built with Django and Django REST Framework. This API enables employers to post jobs, candidates to search and apply for positions, and provides complete application tracking functionality.

![Django](https://img.shields.io/badge/Django-4.2-brightgreen)
![Django REST Framework](https://img.shields.io/badge/DRF-3.14-red)
![Python](https://img.shields.io/badge/Python-3.8+-blue)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

## 📁 Project Structure

job_board_project/
│
├── manage.py # Django management script
├── requirements.txt # Python dependencies
├── README.md # Project documentation
│
├── job_board/ # Django project settings
│ ├── init.py
│ ├── settings.py # Project configuration
│ ├── urls.py # Main URL routing
│ ├── wsgi.py # WSGI configuration
│ └── asgi.py # ASGI configuration
│
├── api/ # Main application
│ ├── init.py
│ ├── admin.py # Admin panel configuration
│ ├── apps.py # App configuration
│ ├── models.py # Database models
│ ├── serializers.py # API serializers
│ ├── views.py # API views and logic
│ ├── urls.py # API URL routing
│ └── migrations/ # Database migrations
│ └── init.py
│
├── media/ # Uploaded files
│ ├── company_logos/ # Employer company logos
│ └── resumes/ # Candidate resume files
│
├── screenshots/ # Documentation screenshots
│ ├── api-root.png
│ ├── admin-panel.png
│ ├── job-listings.png
│ ├── registration.png
│ └── applications.png
│
└── venv/ # Virtual environment (not in repo)

---

## 📋 Table of Contents

- [Features](#features)
- [Screenshots](#screenshots)
- [Technology Stack](#technology-stack)
- [Project Structure](#project-structure)
- [Installation & Setup](#installation--setup)
- [API Endpoints](#api-endpoints)
- [Usage Guide](#usage-guide)
- [Database Models](#database-models)
- [Contributing](#contributing)
- [License](#license)

---

## ✨ Features

### 👔 For Employers

- **Company Profile Management** - Create and manage company profiles with logos
- **Job Posting** - Post job listings with detailed descriptions and requirements
- **Application Management** - View and manage all applications for your jobs
- **Status Tracking** - Update application status (Pending → Reviewing → Shortlisted → Accepted/Rejected)
- **Job Management** - Edit, deactivate, or delete job listings

### 👨‍💼 For Candidates

- **Profile Creation** - Build professional profiles with summaries
- **Resume Upload** - Upload resumes (PDF, DOC, DOCX)
- **Skill Showcase** - List your skills and experience
- **Job Search** - Search jobs by keywords, location, and job type
- **Easy Application** - Apply to jobs with cover letters
- **Application Tracking** - Monitor the status of all your applications

### 🔍 Advanced Features

- **Powerful Search** - Full-text search across job titles, descriptions, and requirements
- **Filtering System** - Filter jobs by type (Full-time, Part-time, Contract, Freelance, Internship)
- **Location Search** - Find jobs by location
- **Sorting Options** - Order jobs by date posted, salary range, or title
- **Pagination** - 10 results per page for better performance
- **Duplicate Prevention** - Candidates can't apply twice for the same job

### 🛡️ Security

- **User Authentication** - Secure login and registration system
- **Role-Based Access** - Different permissions for employers and candidates
- **Data Privacy** - Users can only see their own resumes and applications
- **CORS Enabled** - Ready for frontend integration

### 🛠️ Admin Features

- **Django Admin Panel** - Full administrative interface
- **User Management** - Manage all users and profiles
- **Job Moderation** - Review and manage job listings
- **Application Oversight** - Monitor all applications and their statuses

---

## 📸 Screenshots

### API Root Endpoint

![API Root](screenshots/api-root.png)
_The browsable API interface showing all available endpoints_

### Admin Dashboard

![Admin Panel](screenshots/admin-panel.png)
_Django admin interface for managing the platform_

### Job Listings Endpoint

![Job Listings](screenshots/job-listings.png)
_Browsing and searching job listings through the API_

### Registration Form

![Registration](screenshots/registration.png)
_User registration with employer/candidate selection_

### Application Management

![Applications](screenshots/applications.png)
_Viewing and updating job applications_

---

## 🛠️ Technology Stack

| Technology                | Version | Purpose                |
| ------------------------- | ------- | ---------------------- |
| **Python**                | 3.8+    | Programming Language   |
| **Django**                | 4.2+    | Web Framework          |
| **Django REST Framework** | 3.14+   | API Development        |
| **SQLite**                | 3.x     | Database (Development) |
| **django-cors-headers**   | 4.0+    | CORS Management        |
| **django-filter**         | 23.0+   | Advanced Filtering     |
| **Pillow**                | 10.0+   | Image Processing       |

---

---

## 🚀 Installation & Setup

### Prerequisites

- **Python 3.8 or higher** installed on your system
- **pip** (Python package manager)
- **Git** (optional, for cloning)

### Step 1: Clone the Repository

```bash
# Clone the project
git clone <your-repository-url>
cd job_board_project

# OR create a new folder and copy the project files
Step 2: Create Virtual Environment
Windows:

bash
python -m venv venv
venv\Scripts\activate
Mac/Linux:

bash
python3 -m venv venv
source venv/bin/activate
You should see (venv) in your terminal prompt.

Step 3: Install Dependencies
bash
pip install django djangorestframework django-cors-headers pillow django-filter
Or install from requirements.txt (if you have one):

bash
pip install -r requirements.txt
Step 4: Configure the Database
bash
# Create database migrations
python manage.py makemigrations api

# Apply migrations
python manage.py migrate
Step 5: Create Superuser (Admin)
bash
python manage.py createsuperuser
Follow the prompts:

text
Username: admin
Email address: admin@example.com
Password: [choose a secure password]
Password (again): [repeat password]
Step 6: Create Media Directories
Windows:

bash
mkdir media
mkdir media\company_logos
mkdir media\resumes
Mac/Linux:

bash
mkdir -p media/company_logos
mkdir -p media/resumes
Step 7: Run the Development Server
bash
python manage.py runserver
Step 8: Access the Application
API Interface: http://127.0.0.1:8000/api/

Admin Panel: http://127.0.0.1:8000/admin/

Django Welcome Page: http://127.0.0.1:8000/

📡 API Endpoints
Authentication
Method	Endpoint	Description	Auth Required
POST	/api/register/	Register new user	No
GET	/api/auth/login/	Login page	No
POST	/api/auth/login/	Login user	No
GET	/api/auth/logout/	Logout user	Yes
Employer Endpoints
Method	Endpoint	Description	Auth Required
GET	/api/employers/	List all employers	Yes
POST	/api/employers/	Create employer profile	Yes
GET	/api/employers/{id}/	View employer details	Yes
PUT	/api/employers/{id}/	Update employer profile	Yes
DELETE	/api/employers/{id}/	Delete employer profile	Yes
GET	/api/employers/my_profile/	Get current user's profile	Yes
Candidate Endpoints
Method	Endpoint	Description	Auth Required
GET	/api/candidates/	List all candidates	Yes
POST	/api/candidates/	Create candidate profile	Yes
GET	/api/candidates/{id}/	View candidate details	Yes
PUT	/api/candidates/{id}/	Update candidate profile	Yes
DELETE	/api/candidates/{id}/	Delete candidate profile	Yes
GET	/api/candidates/my_profile/	Get current user's profile	Yes
Job Listing Endpoints
Method	Endpoint	Description	Auth Required
GET	/api/jobs/	List all active jobs	No
POST	/api/jobs/	Create job listing	Yes (Employer)
GET	/api/jobs/{id}/	View job details	No
PUT	/api/jobs/{id}/	Update job listing	Yes (Owner)
DELETE	/api/jobs/{id}/	Delete job listing	Yes (Owner)
GET	/api/jobs/my_listings/	View employer's jobs	Yes (Employer)
GET	/api/jobs/search/	Search jobs with filters	No
Resume Endpoints
Method	Endpoint	Description	Auth Required
GET	/api/resumes/	List user's resumes	Yes
POST	/api/resumes/	Upload resume	Yes (Candidate)
GET	/api/resumes/{id}/	View resume details	Yes (Owner)
PUT	/api/resumes/{id}/	Update resume	Yes (Owner)
DELETE	/api/resumes/{id}/	Delete resume	Yes (Owner)
Application Endpoints
Method	Endpoint	Description	Auth Required
GET	/api/applications/	List applications	Yes
POST	/api/applications/	Submit application	Yes (Candidate)
GET	/api/applications/{id}/	View application details	Yes
PATCH	/api/applications/{id}/update_status/	Update status	Yes (Employer)
GET	/api/applications/my_applications/	View candidate's apps	Yes (Candidate)
Search & Filter Examples
bash
# Search by keyword
/api/jobs/search/?search=python developer

# Filter by job type
/api/jobs/?job_type=FT

# Combine search and filters
/api/jobs/search/?search=react&job_type=CT&location=New York

# Sort by salary
/api/jobs/?ordering=salary_range

# Pagination
/api/jobs/?page=2
💻 Usage Guide
1. Register as an Employer
Go to http://127.0.0.1:8000/api/register/

POST the following JSON:

json
{
    "username": "techcompany",
    "email": "hr@techcompany.com",
    "password": "securepass123",
    "password2": "securepass123",
    "first_name": "Sarah",
    "last_name": "Johnson",
    "user_type": "employer",
    "company_name": "Tech Innovations Inc",
    "company_description": "Leading technology solutions provider"
}
2. Post a Job
Login with employer credentials at /api/auth/login/

Go to http://127.0.0.1:8000/api/jobs/

POST:

json
{
    "title": "Senior Python Developer",
    "description": "We are looking for an experienced Python developer...",
    "requirements": "5+ years Python, Django, REST APIs, PostgreSQL",
    "location": "San Francisco, CA",
    "salary_range": "$120,000 - $160,000",
    "job_type": "FT"
}
3. Register as a Candidate
json
{
    "username": "johndev",
    "email": "john@email.com",
    "password": "candidate123",
    "password2": "candidate123",
    "first_name": "John",
    "last_name": "Developer",
    "user_type": "candidate"
}
4. Apply for a Job
First, upload a resume at /api/resumes/

Then apply at /api/applications/:

json
{
    "job": 1,
    "resume": 1,
    "cover_letter": "I am excited to apply for this position..."
}
5. Manage Applications (Employer)
View all applications at /api/applications/

Update status at /api/applications/1/update_status/:

json
{
    "status": "REVIEWING",
    "employer_notes": "Strong candidate, schedule interview"
}
🗄️ Database Models
Entity Relationship Diagram
text
User (Django Built-in)
├── EmployerProfile (One-to-One)
│   ├── company_name
│   ├── company_description
│   ├── company_website
│   └── company_logo
│
├── CandidateProfile (One-to-One)
│   ├── phone_number
│   ├── location
│   ├── professional_summary
│   └── linkedin_url
│
JobListing (Many-to-One with Employer)
├── title
├── description
├── requirements
├── location
├── salary_range
└── job_type

Resume (One-to-One with Candidate)
├── file
├── skills
├── experience_years
└── education

JobApplication (Many-to-One with Job and Candidate)
├── cover_letter
├── status
└── employer_notes
🔧 Troubleshooting
Common Issues
1. "No module named 'api'"

Make sure the api app is in the same directory as manage.py

Check that 'api' is in INSTALLED_APPS in settings.py

2. Migration Errors

bash
# Reset migrations
python manage.py migrate --fake api zero
python manage.py makemigrations api
python manage.py migrate
3. Media Files Not Showing

Ensure media directories exist

Check MEDIA_URL and MEDIA_ROOT in settings.py

Verify URL patterns in urls.py

4. CORS Errors

Confirm corsheaders is in INSTALLED_APPS

Check CORS_ALLOW_ALL_ORIGINS = True in settings.py

5. Server Won't Start

bash
# Check if port is in use
# Windows
netstat -ano | findstr :8000
# Mac/Linux
lsof -i :8000

# Use different port
python manage.py runserver 8080
🚀 Deployment
Quick Deploy to PythonAnywhere (Free)
Sign up at PythonAnywhere

Upload your project files

Set up virtual environment

Configure WSGI file

Set up static and media files

Run migrations

Detailed deployment guide available here

📈 Future Enhancements
JWT Token Authentication

Email notifications for applications

Job bookmarking feature

Advanced analytics dashboard

Interview scheduling system

Company reviews and ratings

Salary comparison tool

Job alerts and recommendations

Mobile app API support

Integration with LinkedIn/Indeed

🤝 Contributing
Contributions are welcome! Here's how you can help:

Fork the repository

Create a feature branch (git checkout -b feature/AmazingFeature)

Commit your changes (git commit -m 'Add some AmazingFeature')

Push to the branch (git push origin feature/AmazingFeature)

Open a Pull Request

```
