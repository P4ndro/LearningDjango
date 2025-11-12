# Django Basics Project

A simple Django web application built to learn the fundamentals of Django web development, including templates, static files, URL routing, and app creation.

## 🚀 Features

- **Home Page**: Welcome page with modern design
- **About Page**: Project information
- **Posts App**: Full CRUD functionality for blog posts
  - Create, Read, Update, Delete posts
  - Image upload support
  - Slug-based URLs
  - Delete confirmation dialog
- **User Authentication**: Complete registration and login system
  - Custom registration form with email and name fields
  - Login/Logout functionality
  - Protected routes (login required)
  - User-specific features
- **Custom Forms**: ModelForms with validation
  - Custom User Registration Form
  - Post Creation/Edit Forms
- **Template Inheritance**: Using Django's template system with a base layout
- **Static Files**: Custom CSS and JavaScript
- **Modern UI**: Beautiful gradient design with responsive layout
- **Dynamic Navigation**: Changes based on authentication status
- **Flash Messages**: Success/error messages with animations

## 📋 Prerequisites

Before running this project, make sure you have:

- Python 3.8 or higher
- pip (Python package manager)
- Git

## 🔧 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/P4ndro/LearningDjango.git
   cd LearningDjango
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**
   - On Windows:
     ```bash
     .\venv\Scripts\Activate.ps1
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

5. **Run migrations**
   ```bash
   python manage.py migrate
   ```

6. **Start the development server**
   ```bash
   python manage.py runserver
   ```

7. **Open your browser** and visit:
   - Homepage: `http://127.0.0.1:8000/`
   - About: `http://127.0.0.1:8000/about/`
   - Posts: `http://127.0.0.1:8000/posts/`
   - Admin: `http://127.0.0.1:8000/admin/`

## 📁 Project Structure

```
myproject/
├── manage.py
├── myproject/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── views.py
│   └── wsgi.py
├── posts/
│   ├── templates/
│   │   └── posts/
│   │       └── posts_list.html
│   ├── views.py
│   ├── urls.py
│   └── models.py
├── templates/
│   ├── layout.html
│   ├── home.html
│   └── about.html
├── static/
│   └── static/
│       ├── css/
│       │   └── style.css
│       └── js/
│           └── main.js
└── requirements.txt
```

## 🎨 Technologies Used

- **Django 5.2.8**: Python web framework
- **HTML5 & CSS3**: Frontend markup and styling
- **JavaScript**: Client-side interactivity
- **SQLite**: Database (default Django database)

## 📝 What I Learned

- Setting up a Django project from scratch
- Creating Django apps (posts, register)
- Using Django's template system and template inheritance
- Serving static files (CSS, JavaScript) and media files
- URL routing, views, and URL namespacing
- Django Models and database migrations
- User authentication system
- Creating custom forms (ModelForms, UserCreationForm)
- Form validation and error handling
- Login required decorators
- Flash messages with Django messages framework
- File uploads (image banners)


## 🔮 Future Enhancements

- [x] Add database models for posts
- [x] Implement CRUD operations for posts
- [x] Add user authentication
- [x] Delete functionality for posts
- [ ] User profiles and post ownership
- [ ] Comments system
- [ ] Categories and tags
- [ ] Search functionality










