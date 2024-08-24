import os
from setuptools import setup, find_packages
from setuptools.command.install import install

class CustomInstallCommand(install):
    """Customized install command to create flashcards directory and files."""
    def run(self):
        # Create the flashcards directory structure
        flashcards_dir = os.path.join(os.getcwd(), 'flashcards', 'test')
        os.makedirs(flashcards_dir, exist_ok=True)

        # Create a test flashcard file
        test_flashcard_file = os.path.join(flashcards_dir, 'example.txt')
        if not os.path.exists(test_flashcard_file):
            with open(test_flashcard_file, 'w') as f:
                f.write("# Score: 0\n")
                f.write("# This is an example flashcard file.\n")
                f.write("# These files need no specific extension, and can be named anything.\n")
                f.write("# Lines that start with '#' are ignored. \n")
                f.write("# Flashcard files always begin with # Score: [int 0-100].\n")
                f.write("# Flashcards follow the below format.\n")
                f.write("question 1: answer 1\n")
                f.write("question 2: answer 2\n")
                f.write("# This line will be ignored.\n")
                f.write("question 3: answer 3\n")


        # Call the standard install procedure
        install.run(self)

setup(
    name='flashcard_appington',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[],
    entry_points={
        'console_scripts': [
            'flashcard-appington=flashcard_appington.main:main',  # Example command-line script
        ],
    },
    cmdclass={
        'install': CustomInstallCommand,
    },
    author='Logan Jacobs',
    author_email='jacolb22@wfu.edu',
    description='A flashcard application for studying Swedish or any other subject.',
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/lbj1533/flashcard_appington',
    python_requires='>=3.6',
    keywords='flashcards education swedish learning',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Education',
        'Topic :: Education'
    ],
)
