""" Setup file to make the content installable """
import setuptools

repo_url = "https://github.com/Jtachan/py-coding-hints.git"

if __name__ == "__main__":
    with open("README.md", "r", encoding="utf-8") as fh:
        long_description = fh.read()

    setuptools.setup(
        url=repo_url,
        name="pymath-tools",
        author="Jaime Gonzalez Gomez",
        author_email="jim.gomez.dnn@gmail.com",
        version="0.0.0",
        python_requires=">=3.8",
        description="The package contains simple and easy usable math functions "
        "and instances for general use.",
        long_description=long_description,
        long_description_content_type="text/markdown",
        install_requires=[
            "numpy>=1.20.0",
        ],
    )
