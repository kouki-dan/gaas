
from setuptools import setup, find_packages

setup(
    name="gaas",
    version="0.1",
    description="Git as a network storage",
    author="Kouki Saito",
    author_email="dan.addr.skd@gmail.com",
    url="https://github.com/kouki-dan/gaas",
    packages=find_packages(),
    test_suite="test",
    install_requires=[
        "GitPython",
    ],
)

