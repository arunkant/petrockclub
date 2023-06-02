load("@python_deps//:requirements.bzl", "requirement")
load("//tools/pytest:defs.bzl", "pytest_test")

py_library(
    name = "catalog",
    srcs = glob(["src/**/*.py"]),
    imports = ["src"],
    visibility = ["//visibility:public"],
    deps = [],
)

pytest_test(
    name = "catalog_test",
    srcs = glob(["tests/*.py"]),
    deps = [
        ":catalog",
    ],
)