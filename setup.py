from setuptools import setup, find_packages

hypen_e_dot = '-e .'   ## for requirements.txt , to avoid error
req = []      ## list for adding requirements from requirements.txt

def read_requirements(path: str = 'requirements.txt'):
    requirements = []
    with open (path, 'r', encoding='utf-8') as f:
        for line in f:
            line =line.strip()
            if not line or line.startswith('#'):
                                           continue
            if line == '-e .':
                continue
            requirements.append(line)
    return requirements
            
set_ = setup(
    name='v1_app',
    version='0.0.1',
    packages=find_packages(),
    install_requires=read_requirements('requirements.txt'),
    description='A sample python application',
    author='vaishnavi Mane',
    author_email='vaishnavimane2323@gmail.com',
    url='https://github.com/VaishnaviGMane/SML_Project/tree/main')