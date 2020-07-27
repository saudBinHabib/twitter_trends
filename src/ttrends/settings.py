from importlib import import_module

from path import Path

PROJECT_ROOT = Path(import_module('downloader').__path__[0]).abspath()
