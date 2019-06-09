import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="toy_robot",
    version="1.0.0",
    author="Sendhil",
    author_email="sendhil@example.com",
    description="Toy robot simulator",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sendhilg/toy-robot-simulator",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
