load("@rules_python//python:pip.bzl", "compile_pip_requirements")

# This rule adds a convenient way to update the requirements.txt
# lockfile based on the requirements.in.
compile_pip_requirements(
    name = "requirements",
    requirements_in = "requirements.in",
    requirements_txt = "requirements_lock.txt"
)
