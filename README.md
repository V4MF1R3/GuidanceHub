# GuidanceHub Project

## Overview
GuidanceHub is a mentorship platform designed to connect mentees with mentors. Users can request mentorship, accept or decline requests, and view their mentorship connections.

live: [https://guidancehub.onrender.com](https://guidancehub.onrender.com)

## Features
- User authentication (login, registration)
- Role-based access (Mentor, Mentee)
- Mentorship request system
- Manage incoming and outgoing mentorship requests
- View mentorship connections and profiles
- Search and filter mentors based on skills and interests

## Prerequisites
- Python 3.11+
- Django 5.1.4

## Installation

### 1. Clone the repository:
```bash
    git clone https://github.com/your-username/guidancehub.git
    cd guidancehub
```
### 2. Run Build file
```bash
    ./build.sh
```
### 3. Run the development server
```bash
    cd GuidanceHub
    python manage.py runserver
```

## Directory Structure
```bash
    GuidanceHub
    │
    ├── requirements.txt  # Project dependencies
    ├── build.sh          # Bash script for setting up the environment
    │
    ├── GuidanceHub/      # Main project directory
    │   ├── mentorship/   # Mentorship app containing core functionality
    │   ├── users/         # User management app
    │   ├── staticfiles/   # Static files (CSS, JS, images, etc.)
    │   └── templates/     # Base templates for the project
    │
    ├── db.sqlite3        # SQLite database file
    ├── manage.py         # Django management utility
```

## License
This project is licensed under the MIT License.