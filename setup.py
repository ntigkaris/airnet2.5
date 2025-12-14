from setuptools import setup

with open('README.md','r') as f:
    long_description = f.read()

with open('LICENSE','r') as f:
    license = f.read()

setup(name='airnet2.5',
      version='0.1.0',
      description='Neural net for particulate matter of 2.5 microns or less',
      long_description=long_description,
      license=license,
      author='Alexandros Ntigkaris',
      url='https://github.com/ntigkaris/airnet2.5',
      packages=['airnet2.5'],
      install_requires=['numpy','pandas','openpyxl','matplotlib','scikit-learn','torch','tqdm'])
