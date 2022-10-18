from oak_build import task


@task(
    aliases=[
        "task_1_alias",
        "task_1_another_alias",
    ]
)
def task_1():
    pass


@task
def task_2():
    pass
