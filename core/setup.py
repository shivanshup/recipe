import os
import subprocess
import sys
import getpass

def install_requirements():
    """
    Install the packages listed in requirements.txt.
    """
    try:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-r', 'requirements.txt'])
        print("Requirements installed successfully.")
    except subprocess.CalledProcessError:
        print("Failed to install requirements.")
        sys.exit(1)

def make_migrations():
    """
    Create new migrations based on the changes detected in the models.
    """
    try:
        subprocess.check_call([sys.executable, 'manage.py', 'makemigrations'])
        print("Migrations created successfully.")
    except subprocess.CalledProcessError:
        print("Failed to create migrations.")
        sys.exit(1)

def run_migrations():
    """
    Apply the migrations to the database.
    """
    try:
        subprocess.check_call([sys.executable, 'manage.py', 'migrate'])
        print("Migrations applied successfully.")
    except subprocess.CalledProcessError:
        print("Failed to apply migrations.")
        sys.exit(1)

def create_superuser():
    """
    Create a superuser for the Django admin.
    """
    try:
        username = "admin"
        email = "admin@admin.in"
        password = "admin"
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')  # Replace with your settings module

        import django
        django.setup()

        from django.contrib.auth import get_user_model
        User = get_user_model()

        if User.objects.filter(username=username).exists():
            print(f"Superuser with username '{username}' already exists.")
        else:
            User.objects.create_superuser(username=username, email=email, password=password)
            print("Superuser created successfully.")
    except Exception as e:
        print("Error occured"+ e)
        

if __name__ == "__main__":
    install_requirements()
    make_migrations()
    run_migrations()
    create_superuser()
