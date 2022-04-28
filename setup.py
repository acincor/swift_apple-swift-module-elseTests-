import setuptools

with open("README.rst", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="swift-module-elseTests",
    version="1.1.7",
    author="Expert Author",
    author_email="Wf6350177@163.com",
    description="add some new project,you can use \"pip install swift-module-elseTests\" command get it.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    project_urls={
        "Bug Tracker": "https://github.com/pypa/sampleproject/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "swift_apple"},
    packages=setuptools.find_packages(where="swift_apple"),
    python_requires=">=2.7",
)
