from typing import Callable

from oak_build.task_runner import TaskRunner

from tests.base_test import BaseTestCase


class TestOakFileLoader(BaseTestCase):
    def test_run_stub_task(self):
        def test_task():
            pass

        result = TaskRunner().run_task(*self._build_args(test_task))

        self.assertEquals(0, result.exit_code)
        self.assertDictEqual({}, result.exit_params)
        self.assertIsNone(result.error)

    def test_run_task_with_exit_code(self):
        def test_task():
            return 123

        result = TaskRunner().run_task(*self._build_args(test_task))

        self.assertEquals(123, result.exit_code)
        self.assertDictEqual({}, result.exit_params)
        self.assertIsNone(result.error)

    def test_run_task_with_exit_params(self):
        def test_task():
            return {
                "param": "value",
            }

        result = TaskRunner().run_task(*self._build_args(test_task))

        self.assertEquals(0, result.exit_code)
        self.assertDictEqual({"param": "value"}, result.exit_params)
        self.assertIsNone(result.error)

    def test_run_task_with_tuple_result(self):
        def test_task():
            return (456, {
                "param": "value",
            })

        result = TaskRunner().run_task(*self._build_args(test_task))

        self.assertEquals(456, result.exit_code)
        self.assertDictEqual({"param": "value"}, result.exit_params)
        self.assertIsNone(result.error)

    def test_run_task_with_exception(self):
        def test_task():
            raise Exception("Test message")

        result = TaskRunner().run_task(*self._build_args(test_task))

        self.assertEquals(1, result.exit_code)
        self.assertDictEqual({}, result.exit_params)
        self.assertIsInstance(result.error, Exception)
        self.assertEquals("Test message", str(result.error))

    def _build_args(self, task: Callable):
        return (
            task.__name__,
            task,
            {
                task.__name__: task
            },
            {},
        )