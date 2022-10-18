from pathlib import Path
from subprocess import run
from unittest import TestCase


class BaseTestCase(TestCase):
    def get_resources_dir(self) -> Path:
        return Path(__file__).parent / "resources"

    @classmethod
    def setUpClass(cls) -> None:
        run(["poetry", "install"], check=True)
