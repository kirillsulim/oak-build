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

    def test_argument_passing(self):
        test_project_dir = self.get_resources_dir() / "argument_passing"
        with TemporaryDirectory() as tmp_dir:

            tmp_dir = Path(tmp_dir)
            copytree(test_project_dir, tmp_dir, dirs_exist_ok=True)
            self.run_oak(tmp_dir, "argument_consumer")

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

    def test_params_no_type_param(self):
        test_project_dir = self.get_resources_dir() / "params"
        with TemporaryDirectory() as tmp_dir:
            tmp_dir = Path(tmp_dir)

            copytree(test_project_dir, tmp_dir, dirs_exist_ok=True)
            self.run_oak(tmp_dir, "no_type_param", params={"param": "test_value"})

            created_file = tmp_dir / "result.txt"
            self.assertEqual("test_value\n", created_file.read_text())

    def test_params_str_param(self):
        test_project_dir = self.get_resources_dir() / "params"
        with TemporaryDirectory() as tmp_dir:
            tmp_dir = Path(tmp_dir)

            copytree(test_project_dir, tmp_dir, dirs_exist_ok=True)
            self.run_oak(tmp_dir, "str_param", params={"param": "Some string value"})

            created_file = tmp_dir / "result.txt"
            self.assertEqual("Some string value\n", created_file.read_text())

    def test_params_int_param(self):
        test_project_dir = self.get_resources_dir() / "params"
        with TemporaryDirectory() as tmp_dir:
            tmp_dir = Path(tmp_dir)

            copytree(test_project_dir, tmp_dir, dirs_exist_ok=True)
            self.run_oak(tmp_dir, "str_param", params={"param": "1234"})

            created_file = tmp_dir / "result.txt"
            self.assertEqual("1234\n", created_file.read_text())

    def test_params_bool_param(self):
        test_project_dir = self.get_resources_dir() / "params"
        with TemporaryDirectory() as tmp_dir:
            tmp_dir = Path(tmp_dir)

            copytree(test_project_dir, tmp_dir, dirs_exist_ok=True)
            self.run_oak(tmp_dir, "bool_param", params={"param": "yes"})

            created_file = tmp_dir / "result.txt"
            self.assertEqual("True\n", created_file.read_text())

    def test_params_enum_param(self):
        test_project_dir = self.get_resources_dir() / "params"
        with TemporaryDirectory() as tmp_dir:
            tmp_dir = Path(tmp_dir)

            copytree(test_project_dir, tmp_dir, dirs_exist_ok=True)
            self.run_oak(tmp_dir, "enum_param", params={"param": "value"})

            created_file = tmp_dir / "result.txt"
            self.assertEqual("VALUE\n", created_file.read_text())

    def test_params_with_default_value(self):
        test_project_dir = self.get_resources_dir() / "params"
        with TemporaryDirectory() as tmp_dir:
            tmp_dir = Path(tmp_dir)

            copytree(test_project_dir, tmp_dir, dirs_exist_ok=True)
            self.run_oak(tmp_dir, "str_param_with_default_value")

            created_file = tmp_dir / "result.txt"
            self.assertEqual("default\n", created_file.read_text())
