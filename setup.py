from setuptools import setup, find_packages


with open('README.rst', encoding='UTF-8') as f:
    readme = f.read()


setup(
    name="sqltools",
    version="0.1.0",
    description='Database backups locally or to S3 like',
    long_description=readme,
    author='Felipe Gusmao',
    author_email='felipe@pinguim.software',
    install_requires=['boto3'],
    packages=find_packages('src'),
    package_dir={'': 'src'},
    entry_points={
        'console_scripts': [
            'sqltools=sqltools.cli:main',
        ]
    }
)
