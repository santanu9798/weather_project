#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    # Help Django find the project if it's nested inside 'weather_project-main'
    base_dir = os.path.dirname(os.path.abspath(__file__))
    nested_repo = os.path.join(base_dir, 'weather_project-main')
    if os.path.exists(nested_repo):
        sys.path.append(nested_repo)

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'weather_project.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
