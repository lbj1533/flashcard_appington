
from setuptools import setup, find_packages

setup(
    name='flashcard_appington',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        # List your project dependencies here
    ],
    entry_points={
        'console_scripts': [
            'flashcard-appington=flashcard_appington.main:main',  # Example command-line script
        ],
    },
    author='Logan Jacobs',
    author_email='jacolb22@wfu.edu',
    description='A flashcard application for studying Swedish.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/lbj1533/flashcard_appington',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
