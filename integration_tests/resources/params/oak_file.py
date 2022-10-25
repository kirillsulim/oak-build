from enum import Enum, auto
from pathlib import Path

from oak_build import task


@task
def no_type_param(param):
    with open(Path("result.txt"), "w") as txt:
        txt.write(f"{param}\n")


@task
def str_param(param: str):
    with open(Path("result.txt"), "w") as txt:
        txt.write(f"{param}\n")


@task
def int_param(param: int):
    with open(Path("result.txt"), "w") as txt:
        txt.write(f"{param}\n")


@task
def bool_param(param: bool):
    with open(Path("result.txt"), "w") as txt:
        txt.write(f"{param}\n")


class TaskEnum(Enum):
    VALUE = auto()


@task
def enum_param(param: TaskEnum):
    with open(Path("result.txt"), "w") as txt:
        txt.write(f"{param.name}\n")
