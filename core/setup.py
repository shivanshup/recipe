import os
import subprocess
import sys

def install_requirements():
    """
    Install the packages listed in requirements.txt.
    """
    try:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-r', 'requirements.txt'])
        print("Requirements installed successfully.")
    except subprocess.CalledProcessError as e:
        print("Failed to install requirements.")
        sys.exit(1)

def make_migrations():
    """
    Create new migrations based on the changes detected in the models.
    """
    try:
        subprocess.check_call([sys.executable, 'manage.py', 'makemigrations'])
        print("Migrations created successfully.")
    except subprocess.CalledProcessError as e:
        print("Failed to create migrations.")
        sys.exit(1)

def run_migrations():
    """
    Apply the migrations to the database.
    """
    try:
        subprocess.check_call([sys.executable, 'manage.py', 'migrate'])
        print("Migrations applied successfully.")
    except subprocess.CalledProcessError as e:
        print("Failed to apply migrations.")
        sys.exit(1)

if __name__ == "__main__":
    install_requirements()
    make_migrations()
    run_migrations()