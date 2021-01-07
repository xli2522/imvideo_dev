import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="imvideo", 
    version="0.0.1",
    author="Xiyuan Li",
    author_email="xli2522@uwo.ca",
    description="Imvideo: Image to video made easy. Powered by OpenCV.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://xli2522.github.io/imvideo/",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
