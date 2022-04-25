# Installation (linux with apt-get)
## Install python and venv
```bash
sudo apt install python3.10
apt-get install python3.10-dev python3.10-venv
python3.10 -m venv venv/
```

## Install requirements
```bash
pip install -r requirements.txt
```

# create DB and super User
```bash
python manage.py makemigrations qaas
python manage.py migrate
python manage.py createsuperuser --email admin@qaas.com --username admin
```

# Run tst server
```bash
python manage.py runserver
```

