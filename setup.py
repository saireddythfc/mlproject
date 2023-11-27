from setuptools import setup, find_packages
from typing import List

HYPEN_E_DOT = '-e .'

def get_requirements(file_path:str) -> list[str]:
    '''
    Returns a list of requirements from the given file path
    '''
    requirements = []
    with open(file_path) as f:
        requirements = f.readlines()
        requirements = [req.replace('\n','') for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
        
    return requirements

setup(
    name='mlproject',
    version='0.0.1',
    author='Sai',
    author_email='saivivaswanthreddy@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
    
)