from setuptools import setup, find_packages

setup(
    name='django_ksu_cas_auth',  # package import name
    version='0.1',
    packages=['django_ksu_cas_auth'],
    include_package_data=True,
    install_requires=[
        'django>=5',  # package requires django 5
        'django-cas-ng>=5',  # cas auth
    ],
    description='django package for auth using KSU cas server',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/alt-cs-lab/django-ksu-cas-auth',
    classifiers=[
        'Framework :: Django',
        'Programming Language :: Python :: 3',
    ],
    python_requires='>=3.10',  # package requires python 3.10
)
