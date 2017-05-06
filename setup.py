from setuptools import setup, find_packages


kw = dict(
    name='xspider',
    version='0.0.3',
    description='simple spider',
    author='intohole',
    author_email='intoblack86@gmail.com',
    url='https://github.com/intoblack/mosquito',
    download_url='https://github.com/intoblack/mosquito',
    platforms='all platform',
    packages=find_packages(exclude=('tests', 'tests.*')),
    include_package_data=True
)

setup(**kw)
