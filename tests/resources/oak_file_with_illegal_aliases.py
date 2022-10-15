from oak_build import task


@task(
    aliases=[
        "task 1 illegal alias",
    ]
)
def task_1():
    pass


@task
def task_2():
    pass
