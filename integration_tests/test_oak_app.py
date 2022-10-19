from pathlib import Path
from shutil import copytree
from subprocess import run
from tempfile import TemporaryDirectory

from integration_tests.base_test import BaseTestCase


class TestOakApp(BaseTestCase):
    def test_file_creator(self):
        test_project_dir = self.get_resources_dir() / "file_creator"
        with TemporaryDirectory() as tmp_dir:
            copytree(test_project_dir, tmp_dir, dirs_exist_ok=True)
            run(["oak", "create_file"], check=True, cwd=tmp_dir)

            created_file = Path(tmp_dir) / "result.txt"
            self.assertEqual("test content\n", created_file.read_text())

    def test_param_passing(self):
        test_project_dir = self.get_resources_dir() / "param_passing"
        with TemporaryDirectory() as tmp_dir:
            copytree(test_project_dir, tmp_dir, dirs_exist_ok=True)
            run(["oak", "param_consumer"], check=True, cwd=tmp_dir)

            created_file = Path(tmp_dir) / "result.txt"
            self.assertEqual("value\n", created_file.read_text())

    def test_file_import(self):
        test_project_dir = self.get_resources_dir() / "file_import"
        with TemporaryDirectory() as tmp_dir:
            copytree(test_project_dir, tmp_dir, dirs_exist_ok=True)
            run(["oak", "collector"], check=True, cwd=tmp_dir)

            created_file = Path(tmp_dir) / "result.txt"
            self.assertEqual("12\n", created_file.read_text())
