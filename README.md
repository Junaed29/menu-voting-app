# Company Dinner Voting System 🍽️

A Django-based web application that allows company employees to vote for their preferred dinner options. This system helps organize company dinners by enabling democratic food selection through a user-friendly voting interface.

## 📋 Table of Contents

- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Docker Setup](#docker-setup)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Database Schema](#database-schema)
- [Contributing](#contributing)
- [License](#license)

## ✨ Features

- **User Authentication**: Secure signup, login, and logout functionality
- **Food Item Management**: Display food items with images, descriptions, and ingredients
- **Voting System**: Employees can vote for their preferred dinner options
- **Vote Tracking**: Real-time vote counts and prevention of duplicate voting
- **Responsive Design**: Mobile-friendly interface using Bootstrap 5
- **Admin Panel**: Django admin interface for managing food items, ingredients, and votes
- **Media Management**: Image upload and serving for food items
- **Docker Support**: Containerized deployment ready

## 🛠️ Tech Stack

- **Backend**: Django 5.2.4 (Python)
- **Database**: PostgreSQL (with psycopg2-binary)
- **Frontend**: HTML, CSS, Bootstrap 5.3.0
- **Image Processing**: Pillow 11.3.0
- **Containerization**: Docker
- **Authentication**: Django's built-in authentication system

## 📁 Project Structure

```
company_dinner_project/
├── companydinner/              # Main Django project
│   ├── __init__.py
│   ├── settings.py            # Project settings
│   ├── urls.py                # Main URL configuration
│   ├── wsgi.py                # WSGI configuration
│   └── asgi.py                # ASGI configuration
├── menu/                      # Main application
│   ├── models.py              # Database models
│   ├── views.py               # View functions
│   ├── urls.py                # App URL patterns
│   ├── admin.py               # Admin configuration
│   ├── migrations/            # Database migrations
│   └── templates/menu/        # HTML templates
│       ├── base.html          # Base template
│       ├── menu.html          # Food listing page
│       ├── login.html         # Login page
│       └── signup.html        # Registration page
├── media/                     # User uploaded files
│   └── food_images/           # Food item images
├── manage.py                  # Django management script
├── requirements.txt           # Python dependencies
├── Dockerfile                 # Docker configuration
└── README.md                  # Project documentation
```

## 📋 Prerequisites

- Python 3.11+
- PostgreSQL 12+
- Docker (optional, for containerized deployment)

## 🚀 Installation

### Local Development Setup

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd company_dinner_project
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up PostgreSQL database**:
   - Create a database named `company_dinner_db`
   - Update database credentials in `companydinner/settings.py`

5. **Run migrations**:
   ```bash
   python manage.py migrate
   ```

6. **Create a superuser**:
   ```bash
   python manage.py createsuperuser
   ```

7. **Start the development server**:
   ```bash
   python manage.py runserver
   ```

8. **Access the application**:
   - Main site: http://localhost:8000
   - Admin panel: http://localhost:8000/admin

## 🐳 Docker Setup

### Quick Start (For Docker Users)

If you already have Docker installed and want to quickly run this project:

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd company_dinner_project
   ```

2. **Build and run with Docker**:
   ```bash
   # Build the Docker image
   docker build -t company-dinner .
   
   # Run the container
   docker run -p 8000:8000 company-dinner
   ```

3. **Access the application**:
   - Open your browser and go to: http://localhost:8000
   - Admin panel: http://localhost:8000/admin

### Docker Setup with Database

For a complete setup with PostgreSQL using Docker Compose:

1. **Create a `docker-compose.yml` file** in the project root directory (same level as `Dockerfile`):
   ```yaml
   version: '3.8'
   services:
     db:
       image: postgres:13
       environment:
         POSTGRES_DB: company_dinner_db
         POSTGRES_USER: postgres
         POSTGRES_PASSWORD: your_password
       ports:
         - "5432:5432"
       volumes:
         - postgres_data:/var/lib/postgresql/data
     
     web:
       build: .
       ports:
         - "8000:8000"
       depends_on:
         - db
       environment:
         - DATABASE_HOST=db
   
   volumes:
     postgres_data:
   ```

2. **Run with Docker Compose**:
   ```bash
   docker-compose up --build
   ```

### Manual Docker Setup

1. **Build the Docker image**:
   ```bash
   docker build -t company-dinner .
   ```

2. **Run the container**:
   ```bash
   docker run -p 8000:8000 company-dinner
   ```

   **Note**: Make sure your PostgreSQL database is accessible from the Docker container. The current configuration uses `host.docker.internal` for database connection.

## 💻 Usage

### For Employees

1. **Registration**: Create an account using the signup form
2. **Login**: Access the system with your credentials
3. **Browse Menu**: View available food options with images and descriptions
4. **View Ingredients**: Click on "Ingredients" to see detailed ingredient lists
5. **Vote**: Click the "Vote" button for your preferred food items
6. **Track Votes**: See real-time vote counts for each food item

### For Administrators

1. **Access Admin Panel**: Navigate to `/admin` and login with superuser credentials
2. **Manage Food Items**: Add, edit, or delete food items with images and descriptions
3. **Manage Ingredients**: Create and manage ingredient lists
4. **Monitor Votes**: View and manage user votes
5. **User Management**: Handle user accounts and permissions

## 🛡️ API Endpoints

| Method | Endpoint | Description | Authentication |
|--------|----------|-------------|----------------|
| GET | `/` | Food list/voting page | Optional |
| POST | `/vote/<food_id>/` | Submit a vote | Required |
| GET/POST | `/signup/` | User registration | Not required |
| GET/POST | `/login/` | User login | Not required |
| POST | `/logout/` | User logout | Required |
| GET | `/admin/` | Admin panel | Admin required |

## 🗄️ Database Schema

### Models

#### User
- Built-in Django User model
- Fields: username, email, password, first_name, last_name

#### Ingredient
- `id`: Primary key
- `name`: Unique ingredient name (CharField, max_length=100)

#### FoodItem
- `id`: Primary key
- `name`: Food item name (CharField, max_length=100)
- `description`: Detailed description (TextField)
- `image`: Food image (ImageField, uploaded to 'food_images/')
- `ingredients`: Many-to-many relationship with Ingredient

#### Vote
- `id`: Primary key
- `user`: Foreign key to User (one-to-many)
- `food_item`: Foreign key to FoodItem (one-to-many)
- `unique_together`: Constraint on (user, food_item) - prevents duplicate votes

### Relationships

- **User ↔ Vote**: One-to-many (One user can have multiple votes)
- **FoodItem ↔ Vote**: One-to-many (One food item can receive multiple votes)
- **FoodItem ↔ Ingredient**: Many-to-many (Food items can have multiple ingredients)
- **Unique Constraint**: Each user can vote only once per food item

## 🎨 Frontend Features

- **Responsive Design**: Bootstrap 5 framework for mobile-friendly interface
- **Card Layout**: Food items displayed in an attractive card grid
- **Modal Windows**: Ingredient details shown in Bootstrap modals
- **Vote Badges**: Real-time vote count display
- **Authentication State**: Different UI for logged-in vs anonymous users
- **Form Validation**: Client and server-side form validation

## 🔧 Configuration

### Environment Variables

The application uses the following key settings (in `settings.py`):

- `SECRET_KEY`: Django secret key (change for production)
- `DEBUG`: Debug mode (set to False for production)
- `ALLOWED_HOSTS`: Allowed host names
- `DATABASE_URL`: PostgreSQL connection string

### Media Files

- Media files are stored in the `media/` directory
- Food images are uploaded to `media/food_images/`
- Static files use Django's default static file handling

## 🔐 Security Features

- CSRF protection on all forms
- User authentication and session management
- SQL injection prevention through Django ORM
- XSS protection via Django's template system
- Database constraints to prevent duplicate votes

## 🚀 Deployment Considerations

### Production Checklist

1. Set `DEBUG = False` in settings
2. Configure proper `ALLOWED_HOSTS`
3. Use environment variables for sensitive data
4. Set up proper database with connection pooling
5. Configure static file serving (nginx, whitenoise, etc.)
6. Set up proper logging
7. Use HTTPS in production
8. Regular database backups

### Docker Production

For production Docker deployment:

1. Use multi-stage builds for smaller images
2. Run with a non-root user
3. Use Docker secrets for sensitive data
4. Set up health checks
5. Use docker-compose for multi-container setup

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Commit your changes: `git commit -am 'Add feature'`
4. Push to the branch: `git push origin feature-name`
5. Submit a pull request

## 📝 Development Notes

- The project uses Django 5.2.4 with Python 3.11
- PostgreSQL is configured as the default database
- Bootstrap 5.3.0 provides the responsive UI framework
- The voting system prevents duplicate votes using database constraints
- Media files are handled through Django's default file storage

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 📞 Support

For support and questions:
- Create an issue in the repository
- Contact the development team
- Check the Django documentation for framework-specific questions

---

**Built with ❤️ using Django and Bootstrap**
