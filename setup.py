from setuptools import find_packages, setup

setup(
    name='dionysus',
    version='0.1.4-22',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'flask',
    ],
)
