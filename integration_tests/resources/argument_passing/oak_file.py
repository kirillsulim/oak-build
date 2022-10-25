from pathlib import Path

from oak_build import task


@task
def argument_source():
    return {
        "param": "value",
    }


@task(depends_on=[argument_source])
def argument_consumer(argument_source_param):
    with open(Path("result.txt"), "w") as txt:
        txt.write(f"{argument_source_param}\n")
