import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="eparser",
    version="0.2.2",
    author="Yanbo Zhang",
    author_email="Zhang.Yanbo@asu.edu",
    description="Package for extracting certain plots",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Zhangyanbo/episode_parser",
    project_urls={
        "Bug Tracker": "https://github.com/Zhangyanbo/episode_parser/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"eparser": "eparser", 'reader':'eparser/reader'},
    packages=['eparser', 'reader'],
    python_requires=">=3.6",
)