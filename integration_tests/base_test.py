from pathlib import Path
from subprocess import run
from typing import Dict, Optional
from unittest import TestCase

from oak_build.oak_file import DEFAULT_OAK_FILE


class BaseTestCase(TestCase):
    def get_resources_dir(self) -> Path:
        return Path(__file__).parent / "resources"

    @classmethod
    def setUpClass(cls) -> None:
        run(["poetry", "install"], check=True)

    def run_oak(self, cwd: Path, *tasks, params: Optional[Dict[str, str]] = None) -> None:
        if params is None:
            params_list = ""
        else:
            params_list = " ".join([f"--param \"{key}={value}\"" for key, value in params.items()])

        task_list = " ".join(tasks)
        oak_file = cwd / DEFAULT_OAK_FILE
        command = f"poetry run oak --log-level=debug --file={oak_file} {params_list} {task_list}"
        run(command, check=True, shell=True)
