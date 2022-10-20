from pathlib import Path
from shutil import copytree
from tempfile import TemporaryDirectory

from integration_tests.base_test import BaseTestCase


class TestOakApp(BaseTestCase):
    def test_file_creator(self):
        test_project_dir = self.get_resources_dir() / "file_creator"
        with TemporaryDirectory() as tmp_dir:
            tmp_dir = Path(tmp_dir)

            copytree(test_project_dir, tmp_dir, dirs_exist_ok=True)
            self.run_oak(tmp_dir, "create_file")

            created_file = tmp_dir / "result.txt"
            self.assertEqual("test content\n", created_file.read_text())

    def test_param_passing(self):
        test_project_dir = self.get_resources_dir() / "param_passing"
        with TemporaryDirectory() as tmp_dir:

            tmp_dir = Path(tmp_dir)
            copytree(test_project_dir, tmp_dir, dirs_exist_ok=True)
            self.run_oak(tmp_dir, "param_consumer")

            created_file = tmp_dir / "result.txt"
            self.assertEqual("value\n", created_file.read_text())

    def test_file_import(self):
        test_project_dir = self.get_resources_dir() / "file_import"
        with TemporaryDirectory() as tmp_dir:
            tmp_dir = Path(tmp_dir)

            copytree(test_project_dir, tmp_dir, dirs_exist_ok=True)
            self.run_oak(tmp_dir, "collector")

            created_file = tmp_dir / "result.txt"
            self.assertEqual("12\n", created_file.read_text())
