<<<<<<< HEAD
#!/nix/store/lwzzgbnj41d657lpxczk6l5f7d5zcnj1-python3-3.10.11/bin/python
=======
#!/nix/store/pa7ad0v5hs8amap6j09dh72cwc36l0sv-python3-3.11.3/bin/python
>>>>>>> 1676cc63 (add)
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "library.settings.dev")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
