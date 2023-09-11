from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .'

def get_requirement(file_path:str)->List[str]:
    requirement=[]
    with open(file_path) as file_obj:
        requirement=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirement]

        if HYPEN_E_DOT  in requirements:
            requirment.remove()

        return requirements

setup(
     name= 'DiamondPricePrediction',
     version='0.0.1',
     author='Sudhir',
     author_email='sudhir.rajput2012@gmail.com',
     install_requires=get_requirement('requirement.txt'),
     packages= find_packages()
     )