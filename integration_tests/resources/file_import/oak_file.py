from pathlib import Path

from oak_build import task

from task_1 import task_1
from task_2.task_2 import task_2


@task(
    depends_on=[task_1, task_2]
)
def collector(task_1_result, task_2_result):
    with open(Path("result.txt"), "w") as txt:
        txt.write(f"{task_1_result}{task_2_result}\n")
