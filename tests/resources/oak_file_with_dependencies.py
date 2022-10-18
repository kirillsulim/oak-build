from oak_build import task


@task
def task_1():
    pass


@task
def task_2():
    pass


@task(
    depends_on=[
        "task_1",
        task_2,
    ]
)
def task_3():
    pass
