#!/nix/store/lwzzgbnj41d657lpxczk6l5f7d5zcnj1-python3-3.10.11/bin/python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "library.settings.dev")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
