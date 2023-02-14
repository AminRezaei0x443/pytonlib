import os
from os.path import dirname, join

from setuptools import find_packages, setup

with open(join(dirname(__file__), "README.md"), "r") as f:
    long_description = f.read()


version = '0.0.3'


setup(
    author="Amin Rezaei",
    author_email="AminRezaei0x443@gmail.com",
    name="rift-tonlib",
    version=version,
    packages=find_packages(".", exclude=["tests"]),
    install_requires=["bitarray", "crcset>=0.0.4", "requests>=2.27.1"],
    package_data={
        "rift_tonlib": [
            "distlib/linux/*",
            "distlib/darwin/*",
            "distlib/freebsd/*",
            "distlib/windows/*",
        ],
        "rift_tonlib.utils": [],
        "": ["requirements.txt"],
    },
    zip_safe=True,
    python_requires=">=3.7",
    url="https://github.com/AminRezaei0x443/pytonlib",
    description="Python API for TON (Telegram Open Network)",
    long_description_content_type="text/markdown",
    long_description=long_description,
)
