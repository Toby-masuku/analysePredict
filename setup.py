from setuptools import setup, find packages

setup(
    name='Group_6_predict',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='This package extract tweets',
    long_description=open('README.md').read(),
    install_requires=['numpy'],['pandas]
    url='https://github.com/<username>/<package-name>',
    authors='Christopher Mahlangu','Marcio Maluka','Phiwayinkosi Hlatshwayo','Toby Masuku','Tumisang Sentle'