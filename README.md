# Neighborhood

## By [Alphonce Kipngeno](https://github.com/Kips-alih) ,January 2022

## Description

The web application that allows you to be in the loop about everything happening in your neighborhood.

## Setup/InstallationDate posted: Instructions

### To get the project into your local machine

* Open your terminal
* Create a folder and navigate to the folder you created.
* Run `https://github.com/Kips-alih/awwards.git`
* Run `cd neighborhood` command to confirm it was successfully cloned.
* Run `virtualenv virtual`to create a virtual environment and activate by running `source virtual/bin/activate`

* Run `pip install -r requirements.txt` to Install the requirements.

### Testing the application

* Setup the database name,user, password and host.
* Make migrations using the command `Python manage.py makemigrations`
* Then migrate the changes using the command `Python manage.py migrate`
* Then test the application by running the command `Python manage.py test`

### Running the application

* Run `Python manage.py runserver`

## User Stories

Here are some user stories:

* Sign in with the application to start using.
* Set up a profile about me and a general location and my neighborhood name.
* Find a list of different businesses in my neighborhood.
* Find Contact Information for the health department and Police authorities near my neighborhood.
* Create Posts that will be visible to everyone in my neighborhood.
* Change My neighborhood when I decide to move out.
* Only view details of a single neighborhood.

## Technologies used

* Python3.8
* Django2.2.4

## Support and contact details

Reach out to me through the following email addresses:

* alphonce.kipngeno@student.moringaschool.com.
* alphoncekipngeno@gmail.com.

### License

* LICENSED UNDER  [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE).
