from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='amazon_data',
    version='0.0.1',
    description='A python package to get amazon product and search data in json form. The package does not require any API keys as it works by scraping the amazon page.',
    py_modules=["amazon_data"],
    package_dir={'': 'amazon_data'},
    extras_require={
        "dev": [
            "pytest >= 3.7",
            "check-manifest",
            "twine"
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    python_requires='>=3',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Anup Kumar Panwar",
    author_email="1anuppanwar@gmail.com",
    url="https://github.com/AnupKumarPanwar/amazon_data"
)
