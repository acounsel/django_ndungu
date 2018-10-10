import os

os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE", "django_ndungu.settings")

from development_fabfile.fabfile import *
from .fab_tasks import *