from setuptools import setup, find_packages
import codecs
import os

VERSION = '0.0.3'
DESCRIPTION = 'Converts ipynb to py and vice versa, also syncs them'

# Setting up
setup(
    name="py2ipynb2py",
    version=VERSION,
    author="harshit5674 (Harshit Verma)",
    author_email="<verma08harshit@gmail.com>",
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=[],
    keywords=['python','jupyter','convertor'],
    classifiers=[
	"Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
