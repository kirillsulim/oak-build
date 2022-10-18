from pathlib import Path

from oak_build import task

from task_1 import task_1


@task(
    depends_on=[task_1]
)
def task_2(task_1_result):
    with open(Path("result.txt"), "w") as txt:
        txt.write(f"{task_1_result}\n")
