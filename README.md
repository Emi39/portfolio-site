# Modern Django Portfolio

A production-ready personal portfolio website built with Django 5 and Tailwind CSS. Features a dynamic project case study system, a dark/light mode toggle, and a fully customized admin interface utilizing `django-unfold`.

![Portfolio Preview](static/preview.png)
*(Note: Add a screenshot named preview.png to your static folder for this to show)*

## 🚀 Features

*   **Modern Admin Interface**: Replaced the default Django admin with [Django Unfold](https://github.com/unfoldadmin/django-unfold) for a premium dashboard experience.
*   **Dynamic Content**:
    *   **Projects**: Add case studies with rich text, tags, and images.
    *   **Profile**: Update your bio, social links, and resume from the admin panel without touching code.
    *   **Messages**: Contact form submissions are saved to the database.
*   **Frontend**:
    *   **Tailwind CSS**: Rapid, utility-first styling.
    *   **Dark Mode**: System-aware dark mode with a manual toggle.
    *   **Responsive**: Fully mobile-optimized layout.

## 🛠️ Tech Stack

*   **Backend**: Python 3.10+, Django 5.x
*   **Frontend**: HTML5, Tailwind CSS (CDN)
*   **Database**: SQLite (Dev) / Compatible with Postgres/MySQL (Prod)
*   **Utilities**: `django-cleanup` (auto-deletes old images), `Pillow` (image processing)

## 📦 Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/portfolio-site.git
    cd portfolio-site
    ```

2.  **Create a virtual environment:**
    ```bash
    python -m venv venv
    # Windows
    venv\Scripts\activate
    # Mac/Linux
    source venv/bin/activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run migrations:**
    ```bash
    python manage.py migrate
    ```

5.  **Create a superuser (for admin access):**
    ```bash
    python manage.py createsuperuser
    ```

6.  **Run the development server:**
    ```bash
    python manage.py runserver
    ```

    Open [http://127.0.0.1:8000](http://127.0.0.1:8000) to view the site.
    Access the admin at [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin).

## 🚀 Deployment (PythonAnywhere)

This project is configured for deployment on [PythonAnywhere](https://www.pythonanywhere.com/).

1.  Upload files to PythonAnywhere.
2.  Set `STATIC_URL = '/static/'` and `ALLOWED_HOSTS` in `settings.py`.
3.  Run `python manage.py collectstatic`.
4.  Configure WSGI file and Virtualenv in the Web tab.

## 📄 License

MIT License - feel free to use this for your own portfolio!
