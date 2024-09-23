from setuptools import setup, find_packages

setup(
    name='bt_example',
    version='0.1.0',
    description='A simple backtesting example using the bt library',
    author='Patrick Sheelar',
    packages=find_packages(),
    install_requires=[
        'bt',
        'ffn',
        'matplotlib',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
    ],
)
