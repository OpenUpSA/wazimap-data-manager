import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), "README.md")) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name="data-manager",
    version="0.1",
    packages=find_packages(),
    include_package_data=True,
    install_requires=["django-q==1.0.2", "djangorestframework==3.9.2"],
    license="MIT License",  # example license
    description="Django app to upload datasets into wazimap",
    long_description=README,
    url="https://github.com/OpenUpSA/wazimap-data-manager",
    author="OpenUpSA",
    author_email="webapps@openup.org.za",
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Django",
        "Framework :: Django :: 2.2",  # replace "X.Y" as appropriate
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",  # example license
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
    ],
)
