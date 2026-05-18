# 📅 Event Registration System

A beginner-friendly Django web application for managing event registrations. Users can browse events, register for them, and manage their registrations through a clean web interface.

![Django Version](https://img.shields.io/badge/Django-5.0-green)
![Python Version](https://img.shields.io/badge/Python-3.10%2B-blue)
![License](https://img.shields.io/badge/License-MIT-yellow)
![Database](https://img.shields.io/badge/Database-PostgreSQL%2FSQLite-orange)

---

## ✨ Features

- 👤 **User Authentication** - Register, Login, Logout functionality
- 📋 **Event Listings** - Browse all upcoming events with details
- 🎫 **Event Registration** - Register for events with one click
- ❌ **Cancel Registration** - Cancel registration if plans change
- 📊 **Registration Dashboard** - View all your registered events
- 🛡️ **Admin Panel** - Manage events and view registrations
- 🎨 **Responsive Design** - Works on desktop and mobile devices
- 💾 **PostgreSQL/SQLite Support** - Choose your preferred database

---

## 📸 Screenshots [Coming Soon...........]

### Home Page - Event Listings

```bash
┌─────────────────────────────────────────┐
│ 📅 Event System Events Login/Register │
├─────────────────────────────────────────┤
│ │
│ Upcoming Events │
│ │
│ ┌─────────────────────────────────┐ │
│ │ Science Fair 2026 │ │
│ │ 📅 June 15, 2026 │ │
│ │ 📍 School Auditorium │ │
│ │ [View Details] │ │
│ └─────────────────────────────────┘ │
│ │
│ ┌─────────────────────────────────┐ │
│ │ Sports Day 2026 │ │
│ │ 📅 July 10, 2026 │ │
│ │ 📍 School Playground │ │
│ │ [View Details] │ │
│ └─────────────────────────────────┘ │
└─────────────────────────────────────────┘
```

### Event Registration Flow

Browse Events → View Details → Register → My Registrations → Cancel (if needed)

---

## 🚀 Quick Start Guide

### Prerequisites

Before you begin, ensure you have installed:

- **Python 3.10 or higher** - [Download Python](https://www.python.org/downloads/)
- **Git** (optional) - [Download Git](https://git-scm.com/downloads)
- **PostgreSQL** (optional) - [Download PostgreSQL](https://www.postgresql.org/download/)
  - _If you don't want to install PostgreSQL, the project works with SQLite too!_

### 📥 Installation (Step by Step)

#### Step 1: Clone the Repository

Open your terminal/command prompt and run:

```bash
# Clone the project
git clone https://github.com/your-username/event-registration-system.git

# Navigate to the project folder
cd event-registration-system
If you don't have Git: Download the ZIP file from GitHub and extract it.
```

#### Step 2: Create Virtual Environment

```bash
# Create a virtual environment
python -m venv myenv

# Activate it:
# For Windows:
myenv\Scripts\activate

# For Mac/Linux:
source myenv/bin/activate
You should see (myenv) appear in your terminal.
```

#### Step 3: Install Dependencies

```bash
pip install django psycopg2-binary
If you're using SQLite (simpler option), you only need Django:
```

```bash
pip install django
```

#### Step 4: Choose Your Database

###### Option A: SQLite (Recommended for beginners)

No setup needed! SQLite comes with Python.

```bash
Skip to Step 5.
```

###### Option B: PostgreSQL (For advanced users)

Install PostgreSQL from postgresql.org

---------- Create a database:

sql
-- Open psql or pgAdmin and run:
CREATE DATABASE event_registration;
Open event_platform/settings.py and find the DATABASES section.

Update with your PostgreSQL credentials:

```bash
In python:

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'event_registration',
        'USER': 'postgres',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

#### Step 5: Run Database Migrations

```bash
python manage.py migrate
You should see several "OK" messages as Django creates the database tables.
```

#### Step 6: Create Superuser (Admin Account)

```bash
python manage.py createsuperuser
```

Follow the prompts:

```bash
Username: admin
Email address: admin@example.com
Password: ••••••••••
Password (again): ••••••••••
Remember these credentials! You'll use them to access the admin panel.
```

#### Step 7: Run the Development Server

```bash
python manage.py runserver
You should see:

Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
```

#### Step 8: Open in Browser

Visit: http://127.0.0.1:8000/

🎉 You should see the Event Registration System homepage!

### 📖 How to Use

For Regular Users

##### 1. Create an Account

→ Click "Register" on the navigation bar
→ Fill in username, email, and password
→ Click "Register"
→ You'll be redirected to login page

###### 2. Login

→ Click "Login" on the navigation bar
→ Enter your username and password
→ Click "Login"

###### 3. Browse Events

→ Go to "Events" to see all upcoming events
→ Click on any event to see details

###### 4. Register for an Event

→ Click on an event you're interested in
→ Click "Register Now" button
→ You'll see a success message

###### 5. View Your Registrations

→ Click "My Registrations" in the navigation bar
→ See all events you've registered for

###### 6. Cancel a Registration

→ Go to the event detail page
→ Click "Cancel Registration"
→ Confirm the cancellation

##### For Administrators

###### Access Admin Panel

→ Go to http://127.0.0.1:8000/admin/
→ Login with your superuser credentials

###### Add Events

→ Click "Events" under the EVENTS section
→ Click "ADD EVENT" button
→ Fill in event details
→ Click "SAVE"

###### View Registrations

→ Click "Registrations" under the EVENTS section
→ See all user registrations
→ Filter by event or date

## 📁 Project Structure

```bash
event_system/
├── README.md                    # This file - you're reading it!
├── requirements.txt             # Python dependencies
├── manage.py                    # Django management script
├── event_platform/              # Main project folder
│   ├── __init__.py
│   ├── settings.py              # Project settings & database config
│   ├── urls.py                  # Main URL routing
│   └── wsgi.py                  # Web server interface
├── events/                      # Events app
│   ├── __init__.py
│   ├── admin.py                 # Admin panel configuration
│   ├── apps.py                  # App configuration
│   ├── forms.py                 # User registration form
│   ├── models.py                # Event & Registration models
│   ├── urls.py                  # App URL routing
│   ├── views.py                 # View logic
│   └── templates/               # HTML templates
│       ├── events/
│       │   ├── base.html        # Base template with navigation
│       │   ├── event_list.html  # Event listing page
│       │   ├── event_detail.html# Event detail page
│       │   ├── my_registrations.html # User's registrations
│       │   └── register.html    # User registration page
│       └── registration/
│           └── login.html       # Login page
└── myenv/                       # Virtual environment (not in git)
```

## 🛠️ Technology Stack

#### Technology Purpose

```bash
Django 5.0 Web framework
Python 3.10+ Programming language
PostgreSQL/SQLite Database
HTML/CSS Frontend design
Django Templates Dynamic page rendering
Django Auth User authentication
❓ Common Issues & Solutions
"Port 8000 is already in use"
```
