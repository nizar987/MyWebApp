# My Portfolio - Django Web Application

A modern, responsive portfolio website built with Django and Bootstrap. Showcase your projects, skills, experience, and provide a contact form for potential clients or employers.

## Features

- **Modern Design**: Clean, responsive design with Bootstrap 5
- **Project Showcase**: Display your projects with images, descriptions, and links
- **Skills Section**: Show your technical skills with progress bars
- **Experience Timeline**: Professional experience with company details
- **Contact Form**: Functional contact form with email notifications
- **Admin Panel**: Easy content management through Django admin
- **Responsive**: Mobile-friendly design
- **SEO Optimized**: Meta tags and proper structure

## Technologies Used

- **Backend**: Django 5.2.5
- **Frontend**: Bootstrap 5, HTML5, CSS3, JavaScript
- **Database**: SQLite (can be easily changed to PostgreSQL/MySQL)
- **Image Handling**: Pillow
- **Icons**: Font Awesome
- **Fonts**: Google Fonts (Poppins)

## Installation

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd MyWebApp
   ```

2. **Create and activate virtual environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create superuser**
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server**
   ```bash
   python manage.py runserver
   ```

7. **Access the application**
   - Website: http://127.0.0.1:8000/
   - Admin Panel: http://127.0.0.1:8000/admin/

## Project Structure

```
MyWebApp/
├── main/                    # Main Django app
│   ├── models.py           # Database models
│   ├── views.py            # View functions
│   ├── forms.py            # Contact form
│   ├── admin.py            # Admin configuration
│   └── urls.py             # URL patterns
├── portfolio/              # Django project settings
│   ├── settings.py         # Project settings
│   └── urls.py             # Main URL configuration
├── templates/              # HTML templates
│   ├── base.html           # Base template
│   └── main/               # App-specific templates
├── static/                 # Static files
│   ├── css/                # Stylesheets
│   ├── js/                 # JavaScript files
│   └── images/             # Images
├── media/                  # User-uploaded files
├── manage.py               # Django management script
└── requirements.txt        # Python dependencies
```

## Models

### Project
- Title, description, image
- Technologies used
- GitHub and live demo links
- Creation date and ordering

### Skill
- Name, category, proficiency level
- Categorized by type (Programming, Frameworks, etc.)

### Experience
- Company, position, description
- Start/end dates, current status

### Contact
- Name, email, subject, message
- Timestamp and read status

### About
- Personal information and resume
- Profile image

## Customization

### Personal Information
1. Update the hero section in `templates/main/home.html`
2. Modify contact information in `templates/main/contact.html`
3. Update social media links in the footer

### Styling
- Edit `static/css/style.css` for custom styles
- Modify Bootstrap classes in templates
- Update color scheme in CSS variables

### Content Management
1. Access the admin panel at `/admin/`
2. Add your projects, skills, and experience
3. Upload images and documents
4. Manage contact messages

## Deployment

### Local Development
```bash
python manage.py runserver
```

### Production Deployment
1. Set `DEBUG = False` in settings.py
2. Configure your production database
3. Set up static file serving
4. Configure your web server (Nginx, Apache)
5. Use a production WSGI server (Gunicorn, uWSGI)

### Environment Variables
Create a `.env` file for sensitive settings:
```
SECRET_KEY=your-secret-key
DEBUG=False
ALLOWED_HOSTS=yourdomain.com
DATABASE_URL=your-database-url
```

## Features to Add

- [ ] Blog section
- [ ] Portfolio categories/filtering
- [ ] Testimonials
- [ ] Newsletter subscription
- [ ] Analytics integration
- [ ] Multi-language support
- [ ] Dark mode toggle
- [ ] Portfolio PDF export

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For support, email your.email@example.com or create an issue in the repository.

---

**Happy Coding! 🚀**
