from setuptools import setup, find_packages 
from typing import List

def get_requirements(file_path: str) -> List[str]:

    try:
        """This function will return the list of requirements"""
        with open(file_path) as file_obj:
            requirements = file_obj.readlines()
            requirements = [req.replace("\n", "") for req in requirements]
            
            if "-e ." in requirements:
                requirements.remove("-e .")
        
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        requirements = []

    return requirements

setup(
    name="ML Project-Network security",
    version="0.0.1",
    author="Nikhil Sahu",
    author_email="sahunikhil106@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt")
)