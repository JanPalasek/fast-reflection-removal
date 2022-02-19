import setuptools


with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='fast-reflection-removal',
    version='1.0b1',
    description="",
    long_description=long_description,
    long_description_content_type="text/markdown",
    package_dir={
        "": "src/python"
    },
    install_requires=[
        "numpy",
        "scipy",
        "matplotlib",
    ],
    packages=setuptools.find_packages("src/python"),
    entry_points={
        "console_scripts": ["frr = frr.__main__:main"]
    },
    python_requires=">=3.6"
)
