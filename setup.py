from distutils.core import setup

def readme():
    with open('README.md') as f:
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

from crontab import Crontab

cron = CronTab(user=True)

job = cron.new(command='python /home/ubuntu/apt_hunt/scraper/scraper.py')
job.minute.on(0)
job.hour.on(10)

job = cron.new(command='python /home/ubuntu/apt_hunt/scraper/scraper.py')
job.minute.on(0)
job.hour.on(13)

job = cron.new(command='python /home/ubuntu/apt_hunt/scraper/scraper.py')
job.minute.on(0)
job.hour.on(16)

job = cron.new(command='python /home/ubuntu/apt_hunt/scraper/scraper.py')
job.minute.on(0)
job.hour.on(19)

cron.write()
