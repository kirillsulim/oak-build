from shutil import copytree
from subprocess import run
from tempfile import TemporaryDirectory

from integration_tests.base_test import BaseTestCase


class TestOakApp(BaseTestCase):
    def test_shell_run(self):
        test_project_dir = self.get_resources_dir() / "shell_run"
        with TemporaryDirectory() as tmp_dir:
            copytree(test_project_dir, tmp_dir, dirs_exist_ok=True)
            run(["oak", "run_echo"], check=True, shell=True, cwd=tmp_dir)
