from typing import Callable

from oak_build.task_runner import TaskRunner

from tests.base_test import BaseTestCase


class TestOakFileLoader(BaseTestCase):
    def test_run_stub_task(self):
        def empty_task():
            pass

        result = TaskRunner().run_task(*self._build_args_for_run_task(empty_task))

        self.assertEqual(0, result.exit_code)
        self.assertDictEqual({}, result.exit_params)
        self.assertIsNone(result.error)

    def test_run_task_with_exit_code(self):
        def code_result_task():
            return 123

        result = TaskRunner().run_task(*self._build_args_for_run_task(code_result_task))

        self.assertEqual(123, result.exit_code)
        self.assertDictEqual({}, result.exit_params)
        self.assertIsNone(result.error)

    def test_run_task_with_exit_params(self):
        def dict_result_task():
            return {
                "param": "value",
            }

        result = TaskRunner().run_task(*self._build_args_for_run_task(dict_result_task))

        self.assertEqual(0, result.exit_code)
        self.assertDictEqual({"param": "value"}, result.exit_params)
        self.assertIsNone(result.error)

    def test_run_task_with_tuple_result(self):
        def tuple_result_task():
            return (
                456,
                {
                    "param": "value",
                },
            )

        result = TaskRunner().run_task(*self._build_args_for_run_task(tuple_result_task))

        self.assertEqual(456, result.exit_code)
        self.assertDictEqual({"param": "value"}, result.exit_params)
        self.assertIsNone(result.error)

    def test_run_task_with_exception(self):
        def exception_result_task():
            raise Exception("Test message")

        result = TaskRunner().run_task(*self._build_args_for_run_task(exception_result_task))

        self.assertEqual(1, result.exit_code)
        self.assertDictEqual({}, result.exit_params)
        self.assertIsInstance(result.error, Exception)
        self.assertEqual("Test message", str(result.error))

    def test_run_task_with_parameters(self):
        def task_with_parameters(key: bool):
            return {"result": key}

        result = TaskRunner().run_task(*self._build_args_for_run_task(task_with_parameters, parameters={"key": "True"}))

        self.assertEqual(0, result.exit_code)
        self.assertDictEqual({"result": True}, result.exit_params)

    def test_run_task_with_arguments(self):
        def task_with_arguments(previous_task_key: bool):
            return {"result": previous_task_key}

        result = TaskRunner().run_task(*self._build_args_for_run_task(task_with_arguments, arguments={"previous_task_key": False}))

        self.assertEqual(0, result.exit_code)
        self.assertDictEqual({"result": False}, result.exit_params)

    def _build_args_for_run_task(self, task: Callable, arguments=None, parameters=None):
        if arguments is None:
            arguments = {}
        if parameters is None:
            parameters = {}
        return (
            task.__name__,
            task,
            {task.__name__: task},
            arguments,
            parameters,
        )
