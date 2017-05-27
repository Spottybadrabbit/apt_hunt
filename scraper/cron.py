def main():
    from crontab import CronTab

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

if __name__ == "__main__":
  main()
