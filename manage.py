#!/usr/bin/env python
import os
import sys

if __name__ == '__main__':
#
# Because we replaced "import os" with "import environ", in the settings/base.py file we need to make a change. Instead of...
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
# we will use:
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.local')
#
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.local')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)
