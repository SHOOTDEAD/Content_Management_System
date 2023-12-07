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

cms <br>
├── articles <br>
│   ├── admin.py &nbsp;&nbsp;&nbsp;&nbsp; -> Models registered to admin dashboard <br>
│   ├── apps.py <br>
│   ├── __init__.py <br>
│   ├── migrations <br>
│   │   ├── 0001_initial.py <br>
│   │   ├── 0002_alter_article_files.py <br>
│   │   ├── 0003_alter_article_files.py <br>
│   │   ├── 0004_alter_article_files.py <br>
│   │   └── __init__.py <br>
│   ├── models.py&nbsp;&nbsp;&nbsp;&nbsp;-> Articles model schema is defined here <br>
│   ├── tests.py&nbsp;&nbsp;&nbsp;&nbsp;-> Tests are defined here <br>
│   ├── urls.py&nbsp;&nbsp;&nbsp;&nbsp;-> URLs related to articles are routed here <br>
│   └── views.py&nbsp;&nbsp;&nbsp;&nbsp;-> Article-related functionalities are defined here <br>
├── cms <br>
│   ├── asgi.py <br>
│   ├── __init__.py <br>
│   ├── settings.py&nbsp;&nbsp;&nbsp;&nbsp;-> App is configured here <br>
│   ├── urls.py&nbsp;&nbsp;&nbsp;&nbsp;-> Contains paths from all apps <br>
│   └── wsgi.py <br>
├── writers <br>
│   ├── admin.py <br> 
│   ├── apps.py <br>
│   ├── __init__.py <br>
│   ├── migrations <br>
│   │   └── __init__.py <br>
│   ├── models.py <br>
│   ├── tests.py&nbsp;&nbsp;&nbsp;&nbsp;-> Tests are defined here <br>
│   ├── urls.py&nbsp;&nbsp;&nbsp;&nbsp;-> URLs related to users are routed here <br>
│   └── views.py&nbsp;&nbsp;&nbsp;&nbsp;-> User-related functionalities are defined here <br>
├── static <br>
│   ├── admin&nbsp;&nbsp;&nbsp;&nbsp;-> Admin dashboard configurations <br>
│   │   ├── css <br>
│   │   ├── js <br>
│   │   ├── img <br>
│   └── article&nbsp;&nbsp;&nbsp;&nbsp;-> Article components and User components and Home page <br>
│       └── files&nbsp;&nbsp;&nbsp;&nbsp;-> User-uploaded files are stored here <br>
│   │   ├── css <br>
│   │   ├── img <br>
├── db.sqlite3&nbsp;&nbsp;&nbsp;&nbsp;-> Database <br>
├── manage.py&nbsp;&nbsp;&nbsp;&nbsp;-> Main file <br>
