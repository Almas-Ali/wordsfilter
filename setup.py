from setuptools import setup

README = open('README.md', 'r').read()

classifiers = [
    'Operating System :: MacOS :: MacOS X',
    'Operating System :: Microsoft :: Windows',
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python :: 3",
]

setup(
    name="wordsfilter",
    version="0.1",
    description="Wordsfilter - A powerfull word filter tool for Python 3 (open source).",
    long_description_content_type="text/markdown",
    long_description=README,
    url="https://github.com/almas-ali/wordsfilter",
    author="Md. Almas Ali",
    author_email="almaspr3@gmail.com",
    keyword="wordsfilter, word, filter",
    license="MIT",
    classifiers=classifiers,
    packages=['wordsfilter'],
    install_requires=[],
)
