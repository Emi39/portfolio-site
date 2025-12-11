# populate_db.py
import os
import django
import random
from django.core.files.base import ContentFile
from django.core.management.utils import get_random_secret_key

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "portfolio_site.settings")
django.setup()

from django.contrib.auth.models import User
from core.models import Project, Tag, Profile

def run():
    print("Clearing existing data...")
    Project.objects.all().delete()
    Tag.objects.all().delete()
    Profile.objects.all().delete()
    User.objects.filter(username='admin').delete()

    print("Creating admin user...")
    User.objects.create_superuser('admin', 'admin@example.com', 'admin')

    print("Creating tags...")
    tags = ['Python', 'Django', 'JavaScript', 'React', 'Tailwind CSS', 'PostgreSQL', 'Docker', 'AWS']
    tag_objects = []
    for t in tags:
        tag_objects.append(Tag.objects.create(name=t))

    print("Creating profile...")
    Profile.objects.create(
        name="Alex Developer",
        title="Senior Full Stack Engineer",
        bio_short="I build pixel-perfect, engaging, and accessible digital experiences.",
        bio_long="""I'm a passionate developer with over 5 years of experience in building modern web applications. 
        I specialize in the Django framework and React, creating seamless full-stack solutions. 
        When I'm not coding, you can find me contributing to open source or exploring the latest design trends.""",
        email="alex@example.com",
        github_url="https://github.com/",
        linkedin_url="https://linkedin.com/"
    )

    print("Creating projects...")
    projects_data = [
        {
            "title": "E-Commerce Platform",
            "short": "A full-featured online store with payment processing.",
            "desc": "Built with Django and Stripe, this platform features a custom shopping cart, user dashboard, and inventory management system.",
            "tags": ["Django", "Python", "Stripe", "PostgreSQL"],
            "feat": True
        },
        {
            "title": "Task Master App",
            "short": "Productivity application for remote teams.",
            "desc": "Real-time task updates using WebSockets. Features include Kanban boards, team chat, and file sharing.",
            "tags": ["React", "Django", "Docker"],
            "feat": True
        },
        {
            "title": "Portfolio v1",
            "short": "Previous iteration of my personal website.",
            "desc": "Simple static site built with HTML/CSS before upgrading to this dynamic Django version.",
            "tags": ["HTML", "CSS"],
            "feat": False
        },
        {
            "title": "AI Image Generator",
            "short": "Interface for generating images using Stable Diffusion.",
            "desc": "Connects to an AI model API to generate images based on text prompts. Includes a gallery of generated works.",
            "tags": ["Python", "API", "React"],
            "feat": True
        }
    ]

    for p in projects_data:
        proj = Project.objects.create(
            title=p['title'],
            short_description=p['short'],
            description=p['desc'],
            is_featured=p['feat']
        )
        # Add random tags
        project_tags = [t for t in tag_objects if t.name in p['tags']]
        proj.tags.set(project_tags)
        # Note: We aren't adding images here to keep it simple, placeholders handle it in template
        
    print("Database populated successfully!")

if __name__ == '__main__':
    run()
