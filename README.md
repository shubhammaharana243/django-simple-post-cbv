# 📝 Django Simple Post CBV

A simple post management web application built with **Python and Django**, focusing on Django Class-Based Views (CBVs) and user authentication.

This project demonstrates how Django's Class-Based Views simplify common web development tasks and how users can create and manage posts.

## 🚀 Features

- **Create Posts** — Add posts after logging in.
- **Class-Based Views (CBVs)** — Learn how to use Django's built-in generic views.
- **Database Integration** — Store posts using Django's ORM.
- **Django Admin Panel** — Manage application data through the admin interface.

## 🛠️ Tech Stack

- Python
- Django
- HTML
- CSS
- SQLite
- Git & GitHub

## 📂 Project Setup

Follow these steps to run the project on your local machine.

### 1. Clone the Repository

```bash
git clone https://github.com/shubhammaharana243/django-simple-post-cbv.git
```

### 2. Navigate to the Project Directory

```bash
cd django-simple-post-cbv
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

### 4. Activate the Virtual Environment

**Windows:**

```bash
.\venv\Scripts\Activate.ps1
```

### 5. Install Django

If the project includes a `requirements.txt` file, install its dependencies:

```bash
pip install -r requirements.txt
```

Otherwise, install Django directly:

```bash
pip install django
```

### 6. Apply Database Migrations

```bash
python manage.py migrate
```

This creates the necessary database tables.

## 👤 User Account Setup

Before creating a post, follow these steps.

### Step 1: Create a Normal User Account

Start the development server:

```bash
python manage.py runserver
```

Open the application in your browser:

http://127.0.0.1:8000/

Navigate to the registration or signup page and create a new user account.

**Note:** The registration page must be implemented in the project for this step to work.

### Step 2: Create a Superuser

Stop the development server using `Ctrl + C` and run:

```bash
python manage.py createsuperuser
```

Enter your username, email address (if requested), and password.

The superuser account provides access to Django's administrative interface.

### Step 3: Access the Django Admin Panel

Start the server again:

```bash
python manage.py runserver
```

Open:

http://127.0.0.1:8000/admin/

Log in using your superuser credentials.

### Step 4: Log In and Create a Post

1. Open the application's homepage.
2. Log in using your normal user account.
3. Navigate to the post creation page.
4. Enter the post details.
5. Submit the form to create your post.

**Important:** Creating a superuser does not automatically create a normal user account. These are separate accounts. If your application requires authentication to create posts, log in with a registered user account before creating a post.

## ▶️ Run the Development Server

```bash
python manage.py runserver
```

Visit:

http://127.0.0.1:8000/

## 📚 Learning Objectives

Through this project, I explored:

- Django Class-Based Views.
- User authentication and login workflows.
- Database migrations and Django ORM.
- Creating and handling posts.
- Django's built-in admin interface.
- The basic structure of a Django web application.

## 🎯 Project Goal

The goal of this project is to strengthen my understanding of Django Class-Based Views and build a foundation for developing more advanced web applications.

## 👨‍💻 Author

**Shubham Maharana**

- GitHub: [@shubhammaharana243](https://github.com/shubhammaharana243)
- Project Repository: [Django Simple Post CBV](https://github.com/shubhammaharana243/django-simple-post-cbv.git)

---

⭐ If you find this project helpful, consider giving it a star!