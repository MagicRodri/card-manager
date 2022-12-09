# card-manager

### A basic gift cards manager with django
## Installation

### - Clone this repository
### - cd into card-manager directory
```bash
cd card-manager/
```
### - Create virtual environment and install dependencies
```bash
python -m venv venv
source venv/bin/activate
(venv) pip install -r requirements.txt
```
### - Create .env and provide redis credentials for celery (default is localhost)
```bash
(venv) touch .env
```
### .env sample
```
SECRET_KEY = mysecret
DEBUG = 1
ALLOWED_HOSTS=localhost

CELERY_BROKER_URL=redis://localhost:6379
CELERY_RESULT_BACKEND=redis://localhost:6379
```
### - Run migrations and run server
```bash
(venv) python manage.py migrate
(venv) python manage.py runserver
```
### - Run celery worker (make sure redis is spinned before)

Linux
```bash
(venv) celery -A cardmanager worker -l INFO
```

Windows10+ (Set pool to solo)
```bash
(venv) celery -A cardmanager worker -l INFO --pool=solo
```
### Demo version available on [Card-manager](https://).

## Features to add/improve :
- [ ] 
- [ ]
- [ ]