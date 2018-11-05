from setuptools import setup, find_packages
import olaf_the_beheader


setup(
    name="olaf-the-beheader",
    version=olaf_the_beheader.__version__,
    license="BSD",
    description="OLAF BEHEAD PUNY FILES!",
    author="Dave Hall",
    author_email="dave@etianen.com",
    url="https://github.com/etianen/olaf-the-beheader",
    packages=find_packages(),
    entry_points={
        "console_scripts": ["olaf-the-beheader=olaf_the_beheader.__main__:main"],
    },
)
