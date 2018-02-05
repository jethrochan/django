# django
Django 

To run:
1. Download files
2. Setup the Virtual Environment in your machine "virtualenv mytravels"
3. Start Virtual Environment: "source mytravels/bin/activate"
4. Run "pip3 install -r requirements.txt" to download dependencies
5. Initiate your own settings.py to generate a secret key "django-admin startproject mytravels"
6. Copy the settings.py into the downloaded project mytravels/mytravels directory
7. Make database migrations: "python3 manage.py makemigrations" followed with "python3 manage.py migrate"
8. Run the project: "python3 manage.py runserver 0.0.0.0:8000" 
