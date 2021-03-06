from setuptools import setup, find_packages



PACKAGE = "basecrawler"
NAME = "basecrawler"
DESCRIPTION = "This is the crawler libray"
AUTHOR = "ever391"
AUTHOR_EMAIL = "smart.jin@foxmail.com"
URL = "https://github.com/ever391/basecrawler"
VERSION = __import__(PACKAGE).__version__

requires = [
    'requests',
    'bs4',
    'selenium',
    'Pillow',
    'lxml',
    'jieba'
]

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=open("./README.rst").read(),
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    license="MIT",
    url=URL,
    packages=find_packages(),
    package_data={
        '': ['*.rst','*.txt', "md"],
        'test': ['*.msg'],
        },
    include_package_data=True,
    install_requires=requires,
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
    ],
)
