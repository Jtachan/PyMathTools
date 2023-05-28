""" Setup file to make the content installable """
import setuptools

setuptools.setup(
    name="pymath",
    description="The package contains simple and easy usable math-wrapper "
    "instances for packages as 'numpy' or 'transforms3d'",
    author="Jaime Gonzalez Gomez",
    author_email="jim.gomez.dnn@gmail.com",
    version="0.0.0",
    install_requires=[
        "numpy>=1.20.0",
        "transforms3d>=0.3.1",
    ],
    packages=["pymath"],
)
