from setuptools import setup, find_packages

setup(
    name="langchain",
    version="0.0.1",
    packages=find_packages(where="libs"),
    package_dir={"": "libs"},
)
