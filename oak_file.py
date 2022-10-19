from oak_build import task, run


STYLE_TARGETS = [
    "integration_tests",
    "src",
    "tests",
    "oak_file.py",
]


@task
def unit_tests():
    run("poetry run pytest tests")


@task
def integration_tests():
    run("poetry run pytest integration_tests")


@task(
    depends_on=[
        unit_tests,
        integration_tests,
    ]
)
def tests():
    pass


@task
def black():
    targets = " ".join(STYLE_TARGETS)
    run(f"poetry run black --check {targets}")


@task(depends_on=[
    black,
])
def style():
    pass
