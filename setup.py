import setuptools

with open("README.md", "r", encoding='utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name="lennpy",
    version="0.0.8",
    author="Stefan Zdravkovic",
    author_email="stefan.zdra@gmail.com",
    description="Generate Lenny Faces",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords=['lenny', 'memes'],
    url="https://github.com/Histefanhere/lennpy",
    packages=setuptools.find_packages(),
    license='GNU GPLv3',
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3",
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent"
    ],
    entry_points = {
        'console_scripts': ['lennpy=lennpy.command_line:main']
    }
)
