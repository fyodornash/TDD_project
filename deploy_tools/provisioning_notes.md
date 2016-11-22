Provisioning a new site
======================

##required pkgs:

nginx
python3
git
pip3
virtualenv

eg sudo apt-get install nginx git python3 python3-venv pip3

## Nginx virtual host config

see nginx.template.conf
replace SITENAME with, eg staging.my-domain.com

## Systemd service

see gunicorn-systemd.template.service
replace SITENAME with eg staging.my-domain.com

## folder structure
assume we have a user account at /home/username

/home/username
---sites
	---SITENAME
		---database
		---source
		---static
		---virtualenv
