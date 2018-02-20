from setuptools import setup, find_packages

setup(
    name='flask_platform',
    version='4.0',
    long_description=__doc__,
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'flask_platform=flask_platform.run:runApp',
        ],
    },
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'flask',
    ],
)
