# MN-REST
REST API for getting phones .<br>
For easy access demo sqlitedb is available !

## Setup

1. Download the Repository to your local machine <br>
2. Create a Virtual Environment in the [MN-REST](./) folder with this command below <br>
   `python -m venv venv`
3. Activate the environment with this command <br>
   `.\venv\Scripts\activate`
4. Install the dependencies <br>
   `pip install -r requirements.txt `
5. Start the application by running this command (_Run the command where [manage.py](./manage.py) is
   located_) <br>
   ` python manage.py runserver`
## Features
1. Authentication method is JWT and Custom authentication back-end .
2. login with email, phone and username
3. api endpoint for giving data and filter, ordering and search.
4. send message to other user with RESTAPI .
## Custom commands
1. for migration follow `python manage.py migrate-db` .

## Demo user
You can login with this demo user `username:admin` and `password:admin`.

## Endpoints
for see follow link `http://127.0.0.1:8000/swagger/` .
