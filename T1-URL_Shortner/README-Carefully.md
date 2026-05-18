# ** For First Project [T1-URL_Shortner]**

## 🔗 URL Shortener - Your Own TinyURL!

![Python Version](https://img.shields.io/badge/Python-3.7+-blue?logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-2.0+-green?logo=flask&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-3-orange?logo=sqlite&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

> A complete, beginner-friendly URL shortener built with Python, Flask, and SQLite. Create short links, track clicks, and manage all your links in a beautiful table format!

**Live Demo:** _Run locally on `http://127.0.0.1:8548`_

---

## 📸 Screenshots

| Homepage                                                                                                                              | Admin Table View                                                                                                                               |
| ------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| ![Homepage](https://github.com/SouRav8548/BackendProjects/blob/8c8d95c4357bd594727735c2133a852239eba69b/T1-URL_Shortner/HomePage.png) | ![Admin Table View](https://github.com/SouRav8548/BackendProjects/blob/8c8d95c4357bd594727735c2133a852239eba69b/T1-URL_Shortner/AdminPage.png) |

---

## ✨ Features

### Core Features

- ✅ **Create short links** from long URLs in one click
- ✅ **Auto-generate** 6-character random codes (e.g., `Xk9mQp`)
- ✅ **Instant redirect** to original URLs
- ✅ **Persistent storage** using SQLite database
- ✅ **Beautiful responsive UI** that works on mobile & desktop

### Admin Features (Table View)

- 📊 **Tabular display** of all shortened links
- 🔍 **Real-time search/filter** by short code or URL
- 📈 **Click tracking** - see how many times each link is used
- 📅 **Creation timestamps** for every link
- 🔗 **Direct testing** from the table
- ⚠️ **Bulk delete** with confirmation dialog

### Technical Features

- 🔒 **SQL injection protection** using parameterized queries
- 🚦 **Proper HTTP status codes** (200, 302, 404, 500)
- 📝 **JSON API** for programmatic use
- 🎨 **Gradient design** with smooth animations

---

## 📁 Project Structure

### File Structure

url_shortener/
│
├── app.py # Main Flask application
├── urls.db # SQLite database (auto-created on first run)
├── test.py # Optional CLI testing tool
├── README.md # Project documentation
│
└── templates/
└── index.html # Frontend web interface

### Description of Files

| File/Folder            | Purpose                                                                                 |
| ---------------------- | --------------------------------------------------------------------------------------- |
| `app.py`               | Main Flask application containing routes, logic, and database handling                  |
| `urls.db`              | SQLite database file that stores URL mappings (created automatically when the app runs) |
| `test.py`              | Optional command-line interface (CLI) tool for testing the URL shortener functionality  |
| `README-Carefully.md`  | Project documentation with setup instructions and usage guidelines                      |
| `templates/`           | Directory containing HTML template files                                                |
| `templates/index.html` | Frontend web interface for users to interact with the URL shortener                     |

## How to Run This Project on Your Local Machine

### Prerequisites

Make sure you have the following installed on your system:

- **Python 3.7 or higher** ([Download Python](https://www.python.org/downloads/))
- **pip** (Python package installer, comes with Python)

### Step-by-Step Setup Instructions

#### Option 1: Clone with Git (Recommended)

```bash
git clone https://github.com/yourusername/url_shortener.git
cd url_shortener
```

#### Option 2: Download as ZIP

Click the green "Code" button on the GitHub repository page

Select "Download ZIP"

Extract the ZIP file to a folder on your computer

Open your terminal/command prompt and navigate to the extracted folder:

```bash
cd path/to/url_shortener

Installation & Running

1. Create a Virtual Environment (Recommended)----[In CMD]

On Windows:

python -m venv venv
venv\Scripts\activate


On macOS/Linux:

python3 -m venv venv
source venv/bin/activate


2. Install Required Dependencies

pip install flask
Note: This project only requires Flask. SQLite comes built-in with Python, so no additional database installation is needed.


3. Run the Application

python app.py
You should see output similar to:

text
 * Running on http://127.0.0.1:8548
 * Running on http://localhost:8548


4. Access the Application
Open your web browser and go to:

text
http://localhost:8548
You should now see the URL shortener web interface!
```

### How to Use the Application

Shorten a URL: Enter a long URL in the input field and click "Shorten"

Get the short URL: The application will generate a unique short URL

Use the short link: Copy the shortened URL and paste it in your browser - it will redirect to the original long URL

```bash
Running with Different Options
Run on a different port:

python app.py
(Then modify app.run(port=8548) to your desired port in app.py)


Run with debug mode enabled (auto-reloads on code changes):

python app.py
(Set debug=True in app.py)

Testing the Application (Optional)
If you want to test the URL shortener functionality via command line:


python test.py
Troubleshooting
Issue	Solution
ModuleNotFoundError: No module named 'flask'	Run pip install flask
Address already in use	Port 8548 is busy. Change the port in app.py
Permission denied	Try running with python instead of python3 or vice versa
urls.db not found	The database is created automatically when you first run app.py
Project Structure After Running
Once you run the application, the project will look like this:
```

## This README provides clear, step-by-step instructions that any client (even non-technical ones) can follow to get your URL shortener project running on their local machine.
