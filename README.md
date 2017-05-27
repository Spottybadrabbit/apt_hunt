# Apt Hunt 

This repo features the code needed to set up your own tinder-like swipe application to expedite the apartment hunt over Craigslist posts. 

## Overview
* [Configure](http://amunategui.github.io/idea-to-pitch/) an Apache2 server on an Amazon EC2 instance with read/write permissions to S3, DynamoDB, and SQS
* ssh into this server and clone the project repo into the home directory
* Run the setup.py script
* Edit the [configuration file](scraper/config.py)
* Configure the Flask application
* Allow the scraper to build a collection

## Getting Started
Set up an Amazon EC2 t2.micro instance with Amazon's Linux distro. Consider setting up an IAM role with read/write permissions to S3, DynamoDB, and SQS. Check that the security group allows for access to port 80. Then ssh into the instance with:
```bash
ssh -i /path/to/key.pem ec2-user@public_IP_address
```

Once connected, run the following:

```bash
sudo yum update
sudo yum groupinstall "Development Tools"
sudo yum install libxslt-devel
git clone https://github.com/TrrRdrgz/apt_hunt.git
cd apt_hunt
sudo python setup.py install
```

At this point, you should add your GOOGLE_API_KEY as well as set parameters in the [configuration file](scraper/config.py). Then run the scraper.py script or set sensible crontab jobs by running:

```bash
python scraper/cron.py
```

## Usage
![Alt Text](https://s3-us-west-2.amazonaws.com/mayorquinmachines.ai/images/Apt_hunt.gif)

* Navigate to the EC2 server's IP address
* Register a new user
* Start Swiping!
