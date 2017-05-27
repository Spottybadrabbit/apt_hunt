from distutils.core import setup

def readme():
    with open('README.rst') as f:
        return f.read()

setup(
    name='Apt Hunt',
    version='0.1',
    description='Swipe interface for smart filtered apartment hunting',
    url='https://github.com/TrrRdrgz/apt_hunt',
    packages=['apt_hunt',],
    license='MIT',
    long_description=readme(),
    install_requires=["boto3", "python-crontab", "geopy", "lxml", "requests", "simplejson"]
)
