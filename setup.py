import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="projeto_calc",
    version="0.0.2",
    author="Alex Pereira",
    author_email="alexpnet89@gmail.com",
    description="Teste de empacotamento",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/alexpnet89/calculadora.git",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
