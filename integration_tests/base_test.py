from pathlib import Path
from subprocess import run
from unittest import TestCase

from oak_build.oak_file import DEFAULT_OAK_FILE


class BaseTestCase(TestCase):
    def get_resources_dir(self) -> Path:
        return Path(__file__).parent / "resources"

    @classmethod
    def setUpClass(cls) -> None:
        run(["poetry", "install"], check=True)

    def run_oak(self, cwd: Path, *tasks) -> None:
        task_list = " ".join(tasks)
        oak_file = cwd / DEFAULT_OAK_FILE
        run(f"poetry run oak --log-level=debug --file={oak_file} {task_list}", check=True, shell=True)
