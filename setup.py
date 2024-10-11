from setuptools import setup, find_packages


VERSION = "1.0.0"
DESCRIPTION = "My personal packages"
LONG_DESCRIPTION = "A bunch of tools I frequently use and update"

setup(
    name="myne",
    version=VERSION,
    author="deplanty",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    py_modules=find_packages(),
    install_requires=[],

    # url=,
    # project_urls={},

    keywords=["python"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: Microsoft :: Windows",
        "Topic :: Utilities",
    ]
)
