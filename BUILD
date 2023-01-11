load("@rules_python//python:defs.bzl", "py_binary", "py_library")

load("@my_pip_parse//:requirements.bzl", "requirement")

py_library(
    name = "lib",
    srcs = glob(["*.py"]),
    deps = [
        requirement("requests"),
    ],
)

py_binary(
  name = "main",
  srcs = ["main.py"],
  deps = [":lib"],
)