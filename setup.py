from setuptools import find_packages, setup

setup(
    name="vocabulary_extraction",
    version="0.1",
    zip_safe=False,
    package_dir={"": "src"},
    packages=find_packages(where="src"),
)
