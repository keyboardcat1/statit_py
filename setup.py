import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="statit-keyboardcat",
    version="0.0.1",
    author="Azhar Gana",
    author_email="azhar.gana@yahoo.com",
    description="Utilities for gostatit.com",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/keyboardcat1/statit_py",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU GPLv3 ",
        "Operating System :: OS Independent",
    ],
)
