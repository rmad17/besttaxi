[![Stories in Ready](https://badge.waffle.io/rmad17/besttaxi.png?label=ready&title=Ready)](https://waffle.io/rmad17/besttaxi)
# besttaxi
#### Which taxi should you choose?




###Installation

1. Install virtualenv & virtualenvwrapper (Optional but  *__highly recommended__*). For help in this look into the links.
  * http://www.silverwareconsulting.com/index.cfm/2012/7/24/Getting-Started-with-virtualenv-and-virtualenvwrapper-in-Python
  * http://docs.python-guide.org/en/latest/dev/virtualenvs/
2. Execute 'pip install -r requirements.txt'. If __not__ using `virtualenv` then you __might__  need to execute `sudo pip install -r requirements.txt`.
3. To run execute `python manage.py runserver`.

###Configuration
1. Copy all *_secrets_sample.py to *_secrets.py. Add the configs accordingly. besttaxi/basesecrets.py database is not required currently. Database can be set empty `DATABASES = {}`. 
2. UBER_API_KEY and GOOGLE_MAPS_KEY is required to run uber requests. Use Google Maps Direction API. 

###Development
#### To see all available urls
1. `python manage.py show_urls`
