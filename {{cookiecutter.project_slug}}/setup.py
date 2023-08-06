from setuptools import setup

readme = ""
with open("README.md") as f:
    readme = f.read()
    readme = readme.split("\n")
    readme = [line for line in readme if "<img" not in line]
    readme = "\n".join(readme)

with open("requirements.txt", "r") as f:
    requirements = f.read().splitlines()

with open("requirements-dev.txt", "r") as f:
    dev_requirements = f.read().splitlines()

setup(
    name="{{cookiecutter.project_slug}}",
    version="0.0.1",
    description="{{cookiecutter.project_short_description}}",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/johnnysands/{{cookiecutter.project_slug}}",
    author="Johnny Sands",
    author_email="johnnysands@users.noreply.github.com",
    license="MIT",
    packages=["{{cookiecutter.project_slug}}"],
    install_requires=requirements,
    # dev requirements
    extras_require={"dev": dev_requirements},
    readme="README.md",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ],
)
