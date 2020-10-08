## Medical Booking System

A simple application to manage visits of patients and doctors created with Django.

## General Info

The application consists of a registration and login system. 
After authentication, you can choose the date of your visit from the available dates.

## Technologies
* asgiref==3.2.8
* babel==2.8.0
* coverage==5.1
* dj-database-url==0.5.0
* django-crispy-forms==1.9.1
* django-localflavor==3.0.1
* django-phonenumber-field[phonenumbers]==4.0.0
* django==3.0.7
* gunicorn==20.0.4
* phonenumbers==8.12.5
* psycopg2-binary==2.8.5
* python-stdnum==1.13
* pytz==2020.1
* sqlparse==0.3.1
* whitenoise==5.1.0

## Setup

1. Clone repository
```
git clone https://github.com/MateusBz/medical_booking_system.git
```
2. Install pipenv if you don't have one
```
 pip install pipenv
```
3. Create a virtual environment
```
pipenv shell
```
4. Install dependencies

```
pipenv install
```
4.  Start migrations
```
python manage.py migrate
```

5. Create super user
```
python manage.py createsuperuser
```
6. Run the application
```
python manage.py runserver
```
7. Log in as superuser and add doctor visit date time

8. Create patient and doctor account.

## Demo

https://mbs-mat.herokuapp.com/

If you don't want to create a new account, you can use the test accounts:
user: test_patient password: test_user
user: test_doctor password: test_user



