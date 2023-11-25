# coding=utf-8
from setuptools import setup, find_packages
from pathlib import Path

this_directory = Path('README.md').parent
long_description = (this_directory / "README.md").read_text() + '\n\n' + (this_directory / "CHANGELOG.txt").read_text()

classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Developers',
    'Operating System :: Microsoft :: Windows',
    'Operating System :: Unix',
    'Operating System :: MacOS :: MacOS X',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    "Programming Language :: Python :: 3.6",
    "Programming Language :: Python :: 3.7",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3.9",
    "Programming Language :: Python :: 3.10",
    "Programming Language :: Python :: 3.11",
    "Programming Language :: Python :: 3.12"
]
setup(
    name='masterchicken',
    version='0.0.3',
    description='A basic calculator in "class mathcal:" and csv file reader',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://organicchicken.netlify.app/',
    project_urls={
        "Bug Tracker": "https://github.com/PythonChicken123/masterchicken/issues",
        "Download": "https://pypi.org/project/masterchicken/",
        "License": "https://github.com/PythonChicken123/masterchicken/blob/main/LICENSE",
        "Source Code": "https://github.com/PythonChicken123/masterchicken/",
    },
    author='PythonChicken123',
    author_email='wave6013@hotmail.com',
    license='MIT',
    classifiers=classifiers,
    keywords=['chicken', 'laserchicken', 'netlify', 'calculator'],
    packages=find_packages(),
    python_requires=">=3.6",
    install_requires=[],
    package_data={
        '': ['README.md', 'CHANGELOG.txt'],
    },
    include_package_data=True,  
)
