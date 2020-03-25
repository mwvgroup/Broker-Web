# !/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""Django's command-line utility for administrative tasks."""

import os
import sys
from pathlib import Path

sys.path.insert(0, Path(__file__).resolve().parent / 'broker_web/')


def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'broker_web.main.settings')

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