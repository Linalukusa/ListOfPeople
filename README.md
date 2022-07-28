# ListOfPeople
This app has was developed with Django (Python) and the databse used was Postresql. It allows the user to enter the name of people in a textbox and save the data into the database.
database. Jquery 3.6.0 was used to trigger the submit button, it helped to submit the form and display the data without page refresing. I
Setup

The first thing to do is to clone the repository:

$ git clone https://github.com/gocardless/sample-django-app.git
$ cd ListOfPeople_Project
Create a virtual environment to install dependencies in and activate it:

$ python -m venv ./venv
To activate the virtual environment
$ source env/bin/activate //Mac
$ ./venv/Scripts/activate //Windows
Then install the dependencies:

(env)$ pip install -r requirements.txt
Note the (venv) in front of the prompt. This indicates that this terminal session operates in a virtual environment set up by virtual environment.

Once pip has finished downloading the dependencies:

(env)$ cd ListOfPeople
(env)$ python manage.py runserver
And navigate to http://127.0.0.1:8000/.

To login as an admin, navigate to http://127.0.0.1:8000/admin
Username: People
Password: admin123456

The user interface looks like the following:
