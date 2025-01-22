<div align="center">
  <!-- Logo and Title Section -->
  <a href="https://elearning-django-backend.vercel.app/">
    <img src="https://github.com/user-attachments/assets/7db4ae9c-246f-40b5-a686-1fb69222714b" alt="Elearning Logo" height="100px" width="100px" />
  </a>
  <h1>Elearning-Django 🖥️</h1>
  <p>Backend for the Elearning platform built using <strong>Django REST Framework</strong>. It enables managing courses, students, and content through a <strong>RESTful API</strong>. 🔧</p>

  <!-- Live Demo Section -->
  <h2>
    <a href="https://elearning-django-backend.vercel.app/" target="_blank" style="text-decoration: none; display: inline-block; vertical-align: middle;">
      <picture style="vertical-align: middle;">
        <source srcset="https://fonts.gstatic.com/s/e/notoemoji/latest/1f680/512.webp" type="image/webp">
        <img src="https://fonts.gstatic.com/s/e/notoemoji/latest/1f680/512.gif" alt="🚀" width="28" height="28" style="vertical-align: middle;">
      </picture>
      <span style="vertical-align: middle;"> Live Demo</span>
    </a>
  </h2>

  <p>Check out the available API routes for managing courses, students, and content. See the <a href="#-api-endpoints">API Endpoints</a> section for detailed information. 🔧</p>

  <!-- Badges Section -->
  <div>
    <a href="https://github.com/srikanthkanniyappan/Elearning-Django/blob/main/LICENSE">
      <img alt="GitHub License" src="https://img.shields.io/github/license/srikanthkanniyappan/Elearning-Django?color=green">
    </a>
    <a href="https://github.com/srikanthkanniyappan/Elearning-Django/stargazers">
      <img alt="GitHub Repo stars" src="https://img.shields.io/github/stars/srikanthkanniyappan/Elearning-Django?style=flat&color=yellow">
    </a>
    <a href="https://github.com/srikanthkanniyappan/Elearning-Django/commits/main">
      <img alt="GitHub commit activity" src="https://img.shields.io/github/commit-activity/t/srikanthkanniyappan/Elearning-Django?color=violet">
    </a>
    <a href="https://github.com/srikanthkanniyappan/Elearning-Django/blob/main/README.md">
      <img src="https://img.shields.io/badge/Documentation-Available-blue" alt="Documentation Badge" />
    </a>
  </div>
</div>

## Table of Contents

- 🎯 [Features](#-features)
- 🔧 [Tech Stack](#-tech-stack)
- 📋 [Prerequisites](#-prerequisites)
- 🚀 [Getting Started](#-getting-started)
  - 📥 [Installation](#-installation)
  - 🔐 [Environment Configuration](#-environment-configuration)
- 🏁 [Usage](#-usage)
- 📡 [API Endpoints](#-api-endpoints)
- 📁 [Folder Structure](#-folder-structure)
- 🌍 [Deployment](#-deployment)
- 💖 [Donate](#-donate)
- 📜 [License](#-license)
- 📝 [Author](#-author)

## 🎯 Features

- 🔑 **Role-Based Access Control**: Secure multi-user support for Students, Teachers, and Admins, each with role-specific permissions.
- 🔓 **Flexible Authentication**: Supports login using either username or email for convenience.
- 🔒 **JWT Token Authentication**: Ensures secure access to API endpoints with robust token-based authentication.
- 📚 **Course Management**: Students can enroll in and view available courses and their materials.
- 🎥 **[Cloudinary Integration](https://cloudinary.com/) for Videos**: Store and serve video content seamlessly using Cloudinary for efficient media management.
- ⚙️ **Admin and Teacher Controls**: APIs for managing users, courses, and other administrative tasks (work in progress).
- 🌐 **RESTful API Design**: Fully compliant with REST principles for scalable and maintainable backend services.
- 📁 **[Neon PostgreSQL Integration](https://neon.tech/)**: Leverages Neon PostgreSQL for scalable, efficient, and reliable database operations.

## 🔧 Tech Stack

- [![Python](https://img.shields.io/badge/Python-%23FFD43B?style=for-the-badge&logo=python&logoColor=%233776AB)](https://www.python.org/)
- [![Django](https://img.shields.io/badge/Django-%23092E20?style=for-the-badge&logo=django&logoColor=white)](https://www.djangoproject.com/)
- [![Django REST Framework](https://img.shields.io/badge/Django%20REST%20Framework-%23ff1709?style=for-the-badge&logo=django&logoColor=white)](https://www.django-rest-framework.org/)
- [![SimpleJWT](https://img.shields.io/badge/SimpleJWT-%2317212b?style=for-the-badge&logo=python&logoColor=white)](https://django-rest-framework-simplejwt.readthedocs.io/)
- [![PostgreSQL](https://img.shields.io/badge/PostgreSQL-%23336791?style=for-the-badge&logo=postgresql&logoColor=white)](https://www.postgresql.org/)
- [![Neon](https://img.shields.io/badge/Neon-%2300C4B5?style=for-the-badge&logo=postgresql&logoColor=white)](https://neon.tech/)
- [![Gunicorn](https://img.shields.io/badge/Gunicorn-%2320232a?style=for-the-badge&logo=gunicorn&logoColor=%2361DAFB)](https://gunicorn.org/)
- [![Cloudinary](https://img.shields.io/badge/Cloudinary-%230073e6?style=for-the-badge&logo=cloudinary&logoColor=white)](https://cloudinary.com/)
- [![Vercel](https://img.shields.io/badge/Vercel-%23000000?style=for-the-badge&logo=vercel&logoColor=white)](https://vercel.com/)

## 📋 Prerequisites

To run the backend of this project locally, ensure you have the following software, tools, and configurations installed:

### 1. **🐍 Python 3.x**

- 🚀 Required for running the backend server and handling dependencies.
- 📥 Download from [Python Official Website](https://www.python.org/).

### 2. **📦 pip (Python Package Installer)**

- 🛠️ Used to manage project dependencies.
- ✅ Check if pip is installed by running `pip -V` in your terminal.

### 3. **🗃️ PostgreSQL Database (Local)**

- 🏡 Required for storing and managing data locally.
- 📥 Download from [PostgreSQL Official Website](https://www.postgresql.org/download/).

### 4. **🟢 Neon Account (Global)**

- 🌍 Required for using the Neon PostgreSQL database for global deployment.
- 📥 Sign up at [Neon](https://neon.tech/).

### 5. **🛠️ Git**

- 🌐 Version control system required to clone the repository.
- 📥 Download from [Git Official Website](https://git-scm.com/).

### 6. **🖋️ Code Editor**

- 💡 Recommended: [PyCharm](https://www.jetbrains.com/pycharm/) or [VS Code](https://code.visualstudio.com/) for Python and Django support.

### 7. **🌐 API Testing Tool**

- 🛠️ **Postman** (for testing API endpoints, if necessary).

### 8. **☁️ Cloudinary Account**

- 🌐 Used for storing media files like images and videos, including course content.
- 📥 Sign up at [Cloudinary](https://cloudinary.com/).
- 💼 Upload your course content and organize files directly within the Cloudinary **Media Library**.

These tools are 🔑 essential for setting up and running the backend of the **Elearning-Django** project locally.

## 🚀 Getting Started

Follow these steps to set up and run the backend project locally:

### 📥 Installation

1. **Clone the Repository**
   - Clone the backend repository from GitHub to your local machine:
     ```bash
     git clone https://github.com/srikanthkanniyappan/Elearning-Django.git
     ```
2. **Navigate to Project Directory**
   - Change to the project directory:
     ```bash
     cd Elearning-Django
     ```
3. **Create a Virtual Environment**
   - Create and activate a Python virtual environment:
     ```bash
     python -m venv venv
     # On Windows:
     venv\Scripts\activate
     # On macOS/Linux:
     source venv/bin/activate
     ```

4. **Install Dependencies**
   - Install the required Python packages listed in `requirements.txt`:
     ```bash
     pip install -r requirements.txt
     ```

### 🔐 Environment Configuration

1. **Create a `.env` File**
   - In the project root directory, create a `.env` file with the following environment variables:

     ```bash
     # Django settings
     DJANGO_SECRET_KEY='your-django-secret-key'  # Use Django secret key generator for this key
     DJANGO_DEBUG=True
     DJANGO_ALLOWED_HOSTS=.vercel.app,127.0.0.1

     # Database settings (use your Neon PostgreSQL URL)
     DATABASE_URL='postgresql://username:password@host:port/database?sslmode=require'

     # Static and Media files
     STATIC_URL=static/
     MEDIA_ROOT=BASE_DIR / 'media'

     # CORS settings
     CORS_ALLOWED_ORIGINS=http://localhost:5173
     ```

   - Replace `your-django-secret-key`, `username`, `password`, `host`, `port`, `database` with your actual credentials.
   
     To generate a **Django Secret Key**, use this Python snippet:
     ```python
     from django.core.management.utils import get_random_secret_key
     print(get_random_secret_key())
     ```

2. **Set Up Your Database (PostgreSQL)**
   - Set up a PostgreSQL database on **Neon** (or use your preferred PostgreSQL provider).
   - The `DATABASE_URL` variable should contain the URL to your database, including the credentials and the SSL mode for secure connections.

## 🏁 Usage

After completing the installation and environment configuration, follow these steps to run and use the application:

### 🔄 Running the Server

1. **Apply Migrations**
   - Run the following commands to apply migrations and create necessary database tables:
     ```bash
     python manage.py makemigrations  # To generate migrations if any changes have been made
     python manage.py migrate         # To apply migrations to the database
     ```

2. **Run the Development Server**
   - Start the development server:
     ```bash
     python manage.py runserver
     ```

3. **Test the API**
   - The server will be accessible at `http://127.0.0.1:8000/`. You can use Postman, Insomnia, or your browser to test the available API endpoints.

## 📡 API Endpoints

Here are the API endpoints for the **Elearning-Django** backend:

### 🔑 Authentication Endpoints

| Method | Endpoint                            | Description                          |
|--------|-------------------------------------|--------------------------------------|
| GET    | `/api/authentication/routes/`       | Get available authentication routes. |
| POST   | `/api/authentication/register/`     | Register a new user.                 |
| POST   | `/api/authentication/login/`        | User login and obtain a token.       |
| POST   | `/api/authentication/login/refresh/`| Refresh access token.                |
| GET    | `/api/authentication/user/profile/` | Get user profile.                    |
| PUT    | `/api/authentication/user/status-update/` | Update user online status.          |
| GET    | `/api/authentication/user/check-online/` | Check user online status.          |

---

### 📚 Course Management Endpoints

| Method | Endpoint                                  | Description                                  |
|--------|------------------------------------------|----------------------------------------------|
| GET    | `/api/courses/routes/`                   | Get available course routes.                 |
| GET    | `/api/courses/all-courses/`              | List all courses.                            |
| GET    | `/api/courses/all-courses-with-status/`  | List courses with enrollment status.         |
| GET    | `/api/courses/course-list/`              | Get enrolled courses.                        |
| GET    | `/api/courses/course-videos/<course_id>/`| Get videos of a specific course.             |
| GET    | `/api/courses/course-details/<course_id>/`| Get details of a specific course.            |
| GET    | `/api/courses/course/<course_id>/last-watched/`| Get last-watched video of a course.        |
| PUT    | `/api/courses/course/<course_id>/last-watched/update/` | Update last-watched video.          |
| GET    | `/api/courses/course-content/<course_id>/watch-history/` | Get course watch history.         |
| GET    | `/api/courses/videos/<video_id>/`        | Get details of a specific video.             |
| GET    | `/api/courses/videos/<video_id>/watch-history/`| Get watch history of a video.          |
| PUT    | `/api/courses/videos/<video_id>/watch-history/update/`| Update watch history of a video.    |
| POST   | `/api/courses/videos/upload/`            | Upload a new video.                          |
| POST   | `/api/courses/enroll/`                   | Enroll in a course.                          |
| PUT    | `/api/courses/enrollment/update/`        | Update course enrollment status.             |

---

### 🌐 Project URLs

| URL                        | Description                                    |
|----------------------------|------------------------------------------------|
| `/admin/`                  | Admin panel for managing the project.          |
| `/api/authentication/`     | Base route for authentication-related APIs.    |
| `/api/courses/`            | Base route for course-related APIs.            |

These endpoints enable seamless interaction between the frontend and backend for authentication and course management.


## 📁 Folder Structure

Below is the standard folder structure of the **Elearning-Django** project:

```plaintext
Elearning-Django/
│
├── authentication/                  # Authentication app for user management
│   ├── migrations/                   # Database migrations for the authentication app
│   ├── __init__.py                   # Python package marker for authentication
│   ├── admin.py                      # Django admin configurations for authentication
│   ├── apps.py                       # App configuration for authentication
│   ├── models.py                     # Database models for user authentication
│   ├── serializers.py                # Serializers for user-related data
│   ├── tests.py                      # Unit tests for authentication features
│   ├── views.py                      # Views handling authentication-related actions
│   └── urls.py                       # URL routing for authentication app
│
├── courses/                          # Courses app for managing courses and course content
│   ├── migrations/                   # Database migrations for the courses app
│   ├── __init__.py                   # Python package marker for courses
│   ├── admin.py                      # Django admin configurations for courses
│   ├── apps.py                       # App configuration for courses
│   ├── models.py                     # Database models for courses and content
│   ├── serializers.py                # Serializers for course-related data
│   ├── tests.py                      # Unit tests for course management features
│   ├── views.py                      # Views handling course-related actions
│   └── urls.py                       # URL routing for courses app
│
├── Elearning/                        # Project-level folder for settings and configurations
│   ├── __init__.py                   # Python package marker for the project
│   ├── asgi.py                       # ASGI application for asynchronous server handling
│   ├── settings.py                   # Django settings for project-wide configurations
│   ├── urls.py                       # Global URL routing for the project
│   └── wsgi.py                       # WSGI application for deployment
│
├── venv/                             # Virtual environment folder (ignore in git)
├── .gitignore                        # Git ignore configuration for unnecessary files
├── vercel.json                       # Configuration file for Vercel deployment
├── manage.py                         # Django management command-line utility
├── requirements.txt                  # List of dependencies for the project
├── .env                              # Environment variable configuration file (for sensitive settings)
└── README.md                         # Project README for setup and documentation
```

## 🌍 Deployment

Follow these steps to deploy the backend application on **Vercel**:

### 1. Create a Vercel Account
   - Sign up or log in to your account at [Vercel](https://vercel.com/).

### 2. Import the GitHub Repository
   - From the Vercel dashboard, click **New Project**.
   - Select **Import Git Repository** and connect your GitHub account.
   - Choose the **Elearning-Django** repository to deploy.

### 3. Configure Environment Variables
   - After selecting the repository, Vercel will prompt you to configure environment variables.
   - Add the following variables:
     - `DJANGO_SECRET_KEY`
     - `DATABASE_URL`
     - `DJANGO_DEBUG` (Set to `False` for production)
     - `DJANGO_ALLOWED_HOSTS` (e.g., `.vercel.app`)
     - `CORS_ALLOWED_ORIGINS` (e.g., `https://elearning-react-frontend.vercel.app`)
### 4. Add a `vercel.json` File
   - Ensure your project contains a `vercel.json` file with the following content:

     ```json
     {
       "builds": [
         {
           "src": "ELearning/wsgi.py",
           "use": "@vercel/python",
           "config": {
             "maxLambdaSize": "15mb",
             "runtime": "python3.11"
           }
         }
       ],
       "routes": [
         {
           "src": "/(.*)",
           "dest": "ELearning/wsgi.py"
         }
       ]
     }
     ```

### 5. Deploy the Project
   - Click **Deploy** and wait for Vercel to build and deploy your project.

### 6. Verify Deployment
   - Once deployment is complete, your Django backend will be accessible at the URL provided by Vercel.

### Notes
   - Ensure your `requirements.txt` includes all dependencies.
   - Handle media files properly (e.g., using **Cloudinary** for media storage).


## 💖 Donate

If you appreciate this project and would like to support its continued development, you can donate via the button below:

<a href="https://www.buymeacoffee.com/srikanthk" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me A Coffee" style="height: 50px !important;width: 200px !important;" ></a>

Your support helps keep the project alive and improves future updates! Thank you for your generosity! 🙏

## 📜 License

This project is licensed under the [MIT License](LICENSE).

## 📝 Author

**Srikanth Kanniyappan** 👨‍💻

- GitHub: [srikanthkanniyappan](https://github.com/srikanthkanniyappan) :octocat:
- LinkedIn: [srikanthkanniyappan](https://www.linkedin.com/in/srikanthkanniyappan) 👔
- X: [@srikanniyappan](https://x.com/SriKanniyappan) 🐦

