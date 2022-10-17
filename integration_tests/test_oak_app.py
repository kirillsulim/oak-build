from pathlib import Path
from shutil import copytree
from subprocess import run
from tempfile import TemporaryDirectory

from integration_tests.base_test import BaseTestCase


class TestOakApp(BaseTestCase):
    @classmethod
    def setUpClass(cls) -> None:
        run(["poetry", "install"], check=True)

    def test_file_creator(self):
        test_project_dir = self.get_resources_dir() / "file_creator"
        with TemporaryDirectory() as tmp_dir:
            copytree(test_project_dir, tmp_dir, dirs_exist_ok=True)
            run(["oak", "create_file"], check=True, cwd=tmp_dir)

            created_file = Path(tmp_dir) / "result.txt"
            self.assertEquals("test content\n", created_file.read_text())
