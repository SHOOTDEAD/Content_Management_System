[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-3.2-green.svg)](https://www.djangoproject.com/)
# Content Management System (CMS)

CMS is a Django-based web application that allows users to write and manage articles on various topics.

## Installation

### Prerequisites

> Make sure you have Python installed on your system. If not, download and install it from [python.org](https://www.python.org/downloads/).

### Setup Virtual Environment (Optional but recommended)

> python -m venv venv

### On Windows:

> venv\Scripts\activate

### On macOS/Linux:

> source venv/bin/activate

### Install Dependencies

> pip install -r requirements.txt

### Database Setup

> python manage.py migrate

### Create Superuser (Admin)

> python manage.py createsuperuser

### Run the Development Server

> python manage.py runserver

> Visit http://localhost:8000/admin/ to access the admin panel and start managing your content.

### Troubleshooting and Support

> If you encounter any difficulties during installation, please refer to the installation video for step-by-step guidance.

### Usage

### Express Your Thoughts
> Create a account and start writing articles. <br>
> Craft your thougths and ideas by creating a article.<br>
> Add images,files to your article.

### Share with the World
> Once your article is ready, publish it. <br>
> Other users can see your articles.

### Directory Structure:

cms
├── articles
│   ├── admin.py       -> Models registered to admin dashboard 
│   ├── apps.py
│   ├── __init__.py
│   ├── migrations
│   │   ├── 0001_initial.py
│   │   ├── 0002_alter_article_files.py
│   │   ├── 0003_alter_article_files.py
│   │   ├── 0004_alter_article_files.py
│   │   └── __init__.py
│   ├── models.py      -> Articles model schema is defined here
│   ├── tests.py       -> Tests are defined here
│   ├── urls.py        -> URLs related to articles are routed here
│   └── views.py       -> Article-related functionalities are defined here
├── cms
│   ├── asgi.py
│   ├── __init__.py
│   ├── settings.py    -> App is configured here
│   ├── urls.py        -> Contains paths from all apps
│   └── wsgi.py
├── writers
│   ├── admin.py 
│   ├── apps.py
│   ├── __init__.py
│   ├── migrations
│   │   └── __init__.py
│   ├── models.py
│   ├── tests.py       -> Tests are defined here
│   ├── urls.py        -> URLs related to users are routed here
│   └── views.py       -> User-related functionalities are defined here
├── static
│   ├── admin           -> Admin dashboard configurations
│   │   ├── css
│   │   ├── js
│   │   ├── img
│   └── article         -> Article components and User components and Home page
│       └── files       -> User-uploaded files are stored here
│   │   ├── css
│   │   ├── img
├── db.sqlite3          -> Database
├── manage.py           -> Main file



.
├── build                   # Compiled files (alternatively `dist`)
├── docs                    # Documentation files (alternatively `doc`)
├── src                     # Source files (alternatively `lib` or `app`)
├── test                    # Automated tests (alternatively `spec` or `tests`)
├── tools                   # Tools and utilities
├── LICENSE
└── README.md
