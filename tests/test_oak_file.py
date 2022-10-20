from oak_build.oak_file import OakFileLoader
from tests.base_test import BaseTestCase


class TestOakFileLoader(BaseTestCase):
    def test_load_missing_file_returns_error(self):
        err_result = OakFileLoader.load_file(
            self.get_resources_dir() / "missing_oak_file.py"
        )

        self.assertTrue(err_result.is_err)
        self.assertTrue(err_result.unwrap_err()[0].startswith("No such file"))

    def test_load_simple_oak_file(self):
        ok_result = OakFileLoader.load_file(
            self.get_resources_dir() / "simple_oak_file.py"
        )

        self.assertTrue(ok_result.is_ok)
        self.assertSetEqual(
            {"task_1", "task_2"},
            set(ok_result.unwrap().tasks.keys()),
        )

    def test_load_oak_file_with_aliases(self):
        ok_result = OakFileLoader.load_file(
            self.get_resources_dir() / "oak_file_with_aliases.py"
        )

        self.assertTrue(ok_result.is_ok)
        self.assertSetEqual(
            {"task_1", "task_2"},
            set(ok_result.unwrap().tasks.keys()),
        )
        self.assertDictEqual(
            {
                "task_1_alias": "task_1",
                "task_1_another_alias": "task_1",
            },
            ok_result.unwrap().aliases,
        )

    def test_return_error_on_illegal_alias(self):
        err_result = OakFileLoader.load_file(
            self.get_resources_dir() / "oak_file_with_illegal_aliases.py"
        )

        self.assertTrue(err_result.is_err)
        self.assertListEqual(
            [
                'Alias "task 1 illegal alias" for task task_1 doesn\'t match alias pattern ^[a-z][a-z0-9_-]*$',
            ],
            err_result.unwrap_err(),
        )

    def test_load_oak_file_with_dependencies(self):
        ok_result = OakFileLoader.load_file(
            self.get_resources_dir() / "oak_file_with_dependencies.py"
        )

        self.assertTrue(ok_result.is_ok)
        self.assertDictEqual(
            {
                "task_1": [],
                "task_2": [],
                "task_3": ["task_1", "task_2"],
            },
            ok_result.unwrap().dependencies,
        )
