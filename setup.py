import os
from setuptools import setup, find_packages

setup(
    name = "Purse",
    version = "0.1.0",
    author = "Ben Moser",
    packages = ["python"] + [os.path.join("python", a) for a in find_packages("python")],
    include_package_data = True
)
