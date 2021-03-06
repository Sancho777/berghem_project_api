# API Change Calculator

Source Code for Berghem Test

This is a simple API to calculate the exact amount of change that must be given to a customer.

The information is stored in a MongoDB database using the Djongo Engine and can be updated and deleted.

I used Django and Django Rest Framework and Djongo as a MongoDB Engine in this project.


# Testing

to make visualization easier the project is deployed in the following link:

http://adrianoms.pythonanywhere.com/api/profile/


# Usage

In the profile page you can create new Change requests and after reloading the page you will see the new Clients on the list.
You can take the id number of the Client and add to the link path to access the update and delete page.

Ex: http://adrianoms.pythonanywhere.com/api/profile/1


# Installation

1 - Install python and add the Python installed directory to the PATH environment variable as C:\Python37\ and C:\Python 37\Scripts.

2 - Open windows command prompt on the directory you want to install:

3 - Git clone the "berghem_project"

4 - Create a virtual env with this command:

\$ python -m venv env

5 - Activate your virtual env with:

\$ env\Scripts\activate

6 - Install requirements using pip:

\$ cd berghem_project_api
\$ cd berghem_project
\$ pip install -r requirements.txt

7 - Run the development server using manage.py from command prompt:

\$ python manage.py collectstatic
\$ python manage.py runserver

Click on the link and add to the adress: '/api/profile/'

Ex: http://127.0.0.1:8000/api/profile/


