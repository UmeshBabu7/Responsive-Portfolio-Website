# Responsive Portfolio Website

A modern, responsive portfolio website built with Django, showcasing projects, skills, and information. Features a clean design with dark mode support and mobile-friendly navigation.

## Features

- **Responsive Design**: Fully responsive layout that works seamlessly on desktop, tablet, and mobile devices
- **Dark Mode Toggle**: Switch between light and dark themes with a single click
- **Mobile Navigation**: Hamburger menu for easy navigation on mobile devices
- **Project Showcase**: Display your projects with images, GitHub links, and demo links
- **Skills Section**: Organize and display technical skills (Frontend & Backend)
- **Contact Integration**: Quick access to LinkedIn and GitHub profiles
- **CV Download**: Direct download link for your resume/CV
- **Smooth Navigation**: Smooth scrolling navigation between sections

## Technologies Used

- **Backend**: Django
- **Database**: SQLite
- **Frontend**: HTML, CSS, JavaScript
- **Icons**: Font Awesome
- **Fonts**: Google Fonts (Poppins)


## Project Structure

```
Responsive-Portfolio-Website/
│
├── assets/                  # Static files (CSS, images, icons)
│   ├── style.css           # Main stylesheet
│   ├── *.JPG               # Project images
│   ├── cv_umeshtamang.pdf              # Resume/CV file
│   └── *.png               # Favicon and icons
│
├── portfolio/              # Django app
│   ├── migrations/         # Database migrations
│   ├── views.py           # View functions
│   ├── urls.py            # URL routing
│   └── models.py          # Database models
│
├── portfolio_site/         # Django project settings
│   ├── settings.py        # Project configuration
│   ├── urls.py            # Main URL configuration
│   └── wsgi.py            # WSGI configuration
│
├── templates/              # HTML templates
│   └── index.html         # Main portfolio page
│
├── db.sqlite3              # SQLite database
├── manage.py               # Django management script
└── README.md               # This file
```
