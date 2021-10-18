import setuptools


with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='fast-reflection-removal',
    version='0.1a',
    description="",
    long_description=long_description,
    long_description_content_type="text/markdown",
    package_dir={
        "": "src/python"
    },
    install_requires=[
        "argparse~=1.4.0",
        "numpy~=1.21.2",
        "scipy~=1.7.1",
        "matplotlib~=3.4",
    ],
    packages=setuptools.find_packages("src/python"),
    scripts=["bin/run.py"],
    python_requires="~=3.8"
)
