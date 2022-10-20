from pathlib import Path
from shutil import copytree
from tempfile import TemporaryDirectory

from integration_tests.base_test import BaseTestCase


class TestOakApp(BaseTestCase):
    def test_shell_run(self):
        test_project_dir = self.get_resources_dir() / "shell_run"
        with TemporaryDirectory() as tmp_dir:
            tmp_dir = Path(tmp_dir)

            copytree(test_project_dir, tmp_dir, dirs_exist_ok=True)
            self.run_oak(tmp_dir, "run_echo")
