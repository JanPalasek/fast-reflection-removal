import setuptools


with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='template_project',
    version='0.1a',
    description="",
    long_description=long_description,
    long_description_content_type="text/markdown",
    package_dir={
        "": "src/python"
    },
    packages=setuptools.find_packages("src/python"),
    scripts=[],
    python_requires="~=3.8"
)
