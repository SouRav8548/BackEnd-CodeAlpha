# 🍽️ Tasty Bites - Restaurant Management System

A beginner-friendly Restaurant Management System built with Django. This project helps restaurant staff manage menus, orders, tables, inventory, and daily reports from a single web application.

![Django Version](https://img.shields.io/badge/Django-5.0-green)
![Python Version](https://img.shields.io/badge/Python-3.8%2B-blue)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

## 📁 Project Structure

```bash
restaurant_project/
│
├── manage.py                    # Django's command-line utility
├── db.sqlite3                   # Database in sqlite
├── README-Carefully.md          # Project documentation (this file)
├── restaurant_env               # Virtual Environment
│
├── tasty_bites/                 # Main project configuration folder
│   ├── __init__.py
│   ├── settings.py              # Project settings and configuration
│   ├── urls.py                  # Main URL routing
│   ├── wsgi.py                  # WSGI configuration for deployment
│   └── asgi.py                  # ASGI configuration
│
└── restaurant/                  # Main application folder
    ├── __init__.py
    ├── admin.py                 # Admin panel model registration
    ├── apps.py                  # App configuration
    ├── models.py                # Database models (Menu, Orders, etc.)
    ├── views.py                 # View functions (business logic)
    ├── urls.py                  # App-specific URL routing
    ├── tests.py                 # Unit tests
    │
    ├── migrations/              # Database migration files
    │   └── __init__.py
    │
    └── templates/               # HTML templates
        └── restaurant/
            └── home.html        # Main dashboard template
```

### Key Files Explained

#### File Purpose

- models.py Defines database tables: MenuItem, Order, OrderItem, Table, Reservation, InventoryItem
- views.py Contains all business logic: menu display, order processing, inventory updates, reports
- urls.py Maps URLs to view functions (both project-level and app-level)
- admin.py Registers models to appear in Django's admin panel
- home.html Frontend interface with JavaScript for API interaction
- settings.py Configuration: database, installed apps, templates, static files

## 📸 Screenshots

### Home Page

![Home Page](screenshots/home.png)
_The main dashboard showing menu, tables, and order placement options_

### Admin Panel

![Admin Panel](screenshots/admin.png)
_Manage all restaurant data from Django's built-in admin interface_

### Menu Display

![Menu Display](screenshots/menu.png)
_View all available dishes with prices and categories_

### Order Placement

![Order Form](screenshots/order.png)
_Place customer orders and see confirmation with total amount_

### Table Availability

![Table Status](screenshots/tables.png)
_Check which tables are available or occupied in real-time_

### Daily Reports

![Daily Report](screenshots/report.png)
_View today's sales summary including total orders and revenue_

---

## ✨ Features

### 🍕 Menu Management

- Add, edit, and remove menu items
- Organize dishes by categories (Appetizers, Main Course, Desserts)
- Set availability status for each item
- Display prices with proper currency formatting

### 📋 Order Processing

- Create new orders with customer details
- Add multiple items with quantities to each order
- Automatic total calculation
- Track order status: Pending → Preparing → Ready → Served → Paid

### 🪑 Table Management

- Manage restaurant tables with seating capacity
- Real-time table availability checking
- Prevent double-booking of occupied tables
- Visual indicators for available/busy tables

### 📦 Inventory Tracking

- Monitor kitchen ingredient stock levels
- Set reorder thresholds for each item
- Automatic low-stock alerts
- Track stock usage and restocking

### 📊 Reporting

- Daily sales reports with total orders and revenue
- Low stock alerts for inventory management
- Order history tracking

### 🔐 Admin Panel

- Secure admin interface at `/admin/`
- Full CRUD operations on all data
- User authentication system
- Easy data management without writing SQL

---

## 🚀 How to Run Locally

Follow these steps to set up the project on your computer:

### Prerequisites

- **Python 3.8 or higher** installed on your system
- **Git** (optional, for cloning the repository)
- **Web browser** (Chrome, Firefox, or any modern browser)

### Step 1: Clone or Download the Project

**Option A: Using Git**

```bash
git clone https://github.com/yourusername/tasty-bites-restaurant.git
cd tasty-bites-restaurant
```

** Option B: Download ZIP**

```bash
Download the project ZIP file and extract it
```

###### --- Open terminal/command prompt in the extracted folder

### Step 2: Create Virtual Environment

On Windows:

```bash
python -m venv restaurant_env
restaurant_env\Scripts\activate
```

On Mac/Linux:

```bash
python3 -m venv restaurant_env
source restaurant_env/bin/activate
```

###### --- You'll see (restaurant_env) appear in your terminal when activated.

### Step 3: Install Dependencies

```bash
pip install django
```

If a requirements.txt file is available:

```bash
pip install -r requirements.txt
```

### Step 4: Set Up the Database

```bash
python manage.py makemigrations
python manage.py migrate
```

### Step 5: Create Admin Account

```bash
python manage.py createsuperuser
```

-----------Enter your desired credentials:

Example:---

```bash
Username: manager
Email address: manager@tastybites.com
Password: your_secure_password
```

### Step 6: Add Sample Data

Run the optional script to populate the database with sample data:

```bash
python manage.py load_sample_data
Or manually add data through the admin panel after starting the server.
```

### Step 7: Start the Server

```bash
python manage.py runserver
```

### Step 8: Access the Application

Open your web browser and visit:

URL Description

```bash
http://127.0.0.1:8000/                              Main restaurant dashboard
http://127.0.0.1:8000/admin/                        Admin panel (login required)
http://127.0.0.1:8000/api/menu/                     View menu JSON API
http://127.0.0.1:8000/api/tables/                   Check table availability
http://127.0.0.1:8000/api/reports/daily/            Daily sales report
http://127.0.0.1:8000/api/alerts/low-stock/         Low stock alerts
```

## 🛠️ Technology Stack

### Backend

Python 3.8+ Core programming language
Django 5.0 Web framework for rapid development
SQLite Default database (built-in, no setup needed)

### Frontend

HTML5 Page structure and content
CSS3 Styling and visual design
JavaScript (Vanilla) Dynamic content loading and API calls
Fetch API Communication with backend endpoints

### Development Tools

Virtual Environment (venv) Isolated Python environment
Django Admin Built-in data management interface
SQLite Browser (optional) View database contents directly

### APIs Built

Endpoint Method Description:

```bash
/api/menu/                 --- GET Retrieve all available menu items
/api/orders/create/        --- POST Create a new customer order
/api/tables/               --- GET Check table availability status
/api/inventory/update/     --- POST Update ingredient stock levels
/api/reports/daily/        --- GET Get today's sales summary
/api/alerts/low-stock/     --- GET List items below reorder level
```
