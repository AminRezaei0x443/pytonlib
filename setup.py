import os
from os.path import dirname, join

from setuptools import find_packages, setup

with open(join(dirname(__file__), "README.md"), "r") as f:
    long_description = f.read()


version = os.environ.get("PYTONLIB_VERSION", "dev")


setup(
    author="K-Dimentional Tree",
    author_email="kdimentionaltree@gmail.com",
    name="pytonlib",
    version=version,
    packages=find_packages(".", exclude=["tests"]),
    install_requires=["bitarray", "crcset>=0.0.3", "requests>=2.27.1"],
    package_data={
        "pytonlib": [
            "distlib/linux/*",
            "distlib/darwin/*",
            "distlib/freebsd/*",
            "distlib/windows/*",
        ],
        "pytonlib.utils": [],
        "": ["requirements.txt"],
    },
    zip_safe=True,
    python_requires=">=3.7",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "License :: Other/Proprietary License",
        "Topic :: Software Development :: Libraries",
    ],
    url="https://github.com/toncenter/pytonlib",
    description="Python API for TON (Telegram Open Network)",
    long_description_content_type="text/markdown",
    long_description=long_description,
)
