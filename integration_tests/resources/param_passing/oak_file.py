from pathlib import Path

from oak_build import task


@task
def param_source():
    return {
        "param": "value",
    }


@task(
    depends_on=[param_source]
)
def param_consumer(param_source_param):
    with open(Path("result.txt"), "w") as txt:
        txt.write(f"{param_source_param}\n")
