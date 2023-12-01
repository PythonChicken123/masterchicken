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
    "Programming Language :: Python :: 3.9",
    "Programming Language :: Python :: 3.10",
    "Programming Language :: Python :: 3.11",
    "Programming Language :: Python :: 3.12"
]
setup(
    name='masterchicken',
    version='0.0.6',
    description='Coop monitoring system with a optimized CSV reader/writer',
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
    keywords=['python', 'chicken', 'egg', 'csv', 'math'],
    packages=find_packages(),
    python_requires=">=3.9",
    install_requires=['lumache', 'bottle-websocket', 'bottle', 'build', 'cmake', 'distlib', 'docutils', 'numpy', 'packaging', 'pandas', 'pyarrow', 'readme-renderer', 'setuptools', 'urllib3', 'wheel'],
    package_data={
        '': ['README.md', 'CHANGELOG.txt', 'masterchicken.png'],
    },
    include_package_data=True,  
)
