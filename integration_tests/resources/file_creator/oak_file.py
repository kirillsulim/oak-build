from pathlib import Path

from oak_build import task


@task
def create_file():
    with open(Path("result.txt"), "w") as txt:
        txt.write("test content\n")
