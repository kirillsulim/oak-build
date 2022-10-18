from oak_build import task, run


@task
def run_echo():
    return run("echo 1")
