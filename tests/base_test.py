from pathlib import Path
from unittest import TestCase


class BaseTestCase(TestCase):
    def get_resources_dir(self) -> Path:
        return Path(__file__).parent / "resources"
