from setuptools import setup, find_packages
from pathlib import Path

def parse_requirements(filename="requirements.txt"):
    """Load requirements from a pip requirements file."""
    with open(filename, "r") as file:
        lines = file.readlines()
    return [
        line.strip() for line in lines
        if line and not line.startswith("#") and line.strip() != "-e ."
    ]

setup(
    name="your_package_name",
    version="0.1.0",
    author="anand singh",
    author_email="anandmehta300@gmail.com",
    url="https://github.com/yourusername/your-repo-name",
    packages=find_packages(),
    install_requires=parse_requirements(),
   
    
)
