# PythonAnywhere Deployment Instructions

Your project files are ready. Follow these steps to deploy on PythonAnywhere.

## 1. Upload Code
You can upload your code using one of these methods:
- **Git (Recommended)**: Push your code to GitHub, then clone it in a PythonAnywhere Bash console.
- **Zip**: Zip the `portfolio_site` folder, upload it via the "Files" tab, and unzip it in a Bash console (`unzip portfolio_site.zip`).

## 2. Virtual Environment
In a PythonAnywhere Bash console:
```bash
# Create virtualenv
mkvirtualenv --python=/usr/bin/python3.10 my-virtualenv

# Install dependencies
workon my-virtualenv
pip install -r requirements.txt
```

## 3. Web App Configuration
1. Go to the **Web** tab.
2. Click **Add a new web app**.
3. Select **Manual configuration** (since we have an existing project) -> select Python 3.10.
4. **Virtualenv**: Enter the path to your virtualenv (e.g., `/home/yourusername/.virtualenvs/my-virtualenv`).
5. **Source code**: Enter the path to your project folder (e.g., `/home/yourusername/portfolio_site`).
6. **WSGI Configuration File**: Click the link to edit. Update it to point to your project:
   ```python
   import os
   import sys

   path = '/home/yourusername/portfolio_site'
   if path not in sys.path:
       sys.path.append(path)

   os.environ['DJANGO_SETTINGS_MODULE'] = 'portfolio_site.settings'

   from django.core.wsgi import get_wsgi_application
   application = get_wsgi_application()
   ```

## 4. Static Files
In the **Web** tab, under **Static files**:
- **URL**: `/static/`
- **Directory**: `/home/yourusername/portfolio_site/staticfiles` (Note: Run `python manage.py collectstatic` in console first!)
- **URL**: `/media/`
- **Directory**: `/home/yourusername/portfolio_site/media`

## 5. Finish
1. Run `python manage.py migrate` in the console.
2. Run `python manage.py collectstatic`.
3. Click the green **Reload** button in the Web tab.
